//! shell 集成。
//!
//! 装在 shell 里的钩子会把命令行内容交给 Miyu 判断：这是一条要执行的命令，
//! 还是一句想问 Miyu 的话？判断在毫秒级发生（人还按着回车），所以这条路要
//! 尽量短。剪贴板粘贴与占位符展开也在这里。

use crate::cli::*;

pub(in crate::cli) fn remove_shell_hooks(paths: &MiyuPaths) -> Result<()> {
    let removed = shell::fish::uninstall(paths)?;
    let removed = shell::bash::uninstall(paths)? || removed;
    let removed = shell::zsh::uninstall(paths)? || removed;
    if !removed {
        println!(
            "{}",
            t(
                "no installed Miyu shell hooks found",
                "未找到已安装的 Miyu shell hook"
            )
        );
    }
    Ok(())
}

/// 在图片所在目录为 `<32hex>.<ext>` 建 `<8hex>.<ext>` 软链,返回短名。
fn short_image_link(path: &std::path::Path, filename: &str) -> Result<String> {
    let (stem, ext) = filename
        .rsplit_once('.')
        .ok_or_else(|| anyhow::anyhow!("no extension"))?;
    if stem.len() <= 8 {
        return Ok(filename.to_string());
    }
    let short_name = format!("{}.{}", &stem[..8], ext);
    let dir = path
        .parent()
        .ok_or_else(|| anyhow::anyhow!("no parent dir"))?;
    let link = dir.join(&short_name);
    let target = std::path::Path::new(filename);
    let up_to_date = std::fs::read_link(&link)
        .map(|existing| existing == target)
        .unwrap_or(false);
    if !up_to_date {
        if link.exists() || link.is_symlink() {
            std::fs::remove_file(&link)?;
        }
        std::os::unix::fs::symlink(target, &link)?;
    }
    Ok(short_name)
}

pub(in crate::cli) fn run_clipboard_paste(paths: &MiyuPaths) -> Result<()> {
    match crate::clipboard::read_clipboard() {
        Ok(crate::clipboard::ClipboardContent::Image(img)) => {
            let path = img.write_temp_file(&paths.cache_dir, 0)?;
            let filename = path.file_name().and_then(|n| n.to_str()).unwrap_or("image");
            // 占位符里的文件名是跨进程找回图片的唯一线索,删不得;但 32 位
            // 哈希名太吵,给它建个 8 位短名软链,占位符打短名,解析端按名
            // 拼路径照样能打开。同前缀撞名就覆盖软链——同目录会定期清理,
            // 真撞上也只是指向最新一张。
            let display_name = match short_image_link(&path, filename) {
                Ok(name) => name,
                Err(_) => filename.to_string(),
            };
            print!("[Image 1: {}]", display_name);
            io::stdout().flush()?;
            Ok(())
        }
        Ok(crate::clipboard::ClipboardContent::ImagePath(path)) => {
            let filename = std::path::Path::new(&path)
                .file_name()
                .and_then(|n| n.to_str())
                .unwrap_or("image");
            let dir = paths.cache_dir.join("clipboard_images");
            std::fs::create_dir_all(&dir)?;
            crate::clipboard::cleanup_clipboard_images(&dir);
            let link_path = dir.join(filename);
            let need_create = if link_path.is_symlink() {
                !link_path.exists()
            } else {
                !link_path.exists()
            };
            if need_create {
                if link_path.exists() || link_path.is_symlink() {
                    std::fs::remove_file(&link_path)?;
                }
                std::os::unix::fs::symlink(&path, &link_path)?;
            }
            print!("[Image 1: {}]", filename);
            io::stdout().flush()?;
            Ok(())
        }
        Ok(crate::clipboard::ClipboardContent::TextPath(path)) => {
            print!("{}", path);
            io::stdout().flush()?;
            Ok(())
        }
        Ok(crate::clipboard::ClipboardContent::Text(text)) => {
            if should_summarize_pasted_text(&text) {
                let index = shell_pasted_text_index(&paths.cache_dir, &text)?;
                let placeholder = pasted_text_placeholder(index, pasted_text_line_count(&text));
                print!("{}", placeholder);
            } else {
                print!("{}", text);
            }
            io::stdout().flush()?;
            Ok(())
        }
        _ => {
            std::process::exit(1);
        }
    }
}

pub(in crate::cli) fn shell_pasted_text_index(
    cache_dir: &std::path::Path,
    text: &str,
) -> Result<usize> {
    let dir = cache_dir.join("clipboard_texts");
    std::fs::create_dir_all(&dir)?;
    let mut index = 1;
    loop {
        let path = dir.join(format!("{index}.txt"));
        if !path.exists() {
            std::fs::write(path, text)?;
            return Ok(index);
        }
        index += 1;
    }
}

pub(in crate::cli) fn shell_message_from_input(
    use_stdin: bool,
    message: Vec<String>,
) -> Result<String> {
    if use_stdin {
        let mut input = String::new();
        io::stdin().read_to_string(&mut input)?;
        Ok(input)
    } else {
        Ok(join_message(message))
    }
}

pub(in crate::cli) fn run_shell_classify(shell_name: &str, message: &str) -> Result<()> {
    if !matches!(shell_name, "fish" | "bash" | "zsh") {
        std::process::exit(2);
    }
    if shell::is_shell_command(message, shell_name) {
        std::process::exit(0);
    }
    std::process::exit(1);
}

pub(in crate::cli) async fn run_shell_intercept(
    paths: &MiyuPaths,
    shell_name: &str,
    message: String,
) -> Result<()> {
    if !matches!(shell_name, "fish" | "bash" | "zsh") {
        bail!("{}: {shell_name}", t("unsupported shell", "不支持的 shell"));
    }
    if message.trim().is_empty() {
        bail!(
            "{}",
            t("not a natural language command", "不是自然语言命令")
        );
    }

    let message = expand_shell_pasted_text_placeholders(paths, &message)?;
    let (clean_message, pasted_images) = extract_image_placeholders(&message);

    let result = if pasted_images.is_empty() {
        // shell-hook keeps landing in the terminal session: that lane is the
        // whole point of typing natural language at the prompt.
        run_chat_with_options(
            paths,
            clean_message,
            None,
            false,
            AgentMode::Normal,
            TurnSession::Current,
        )
        .await
    } else {
        run_chat_with_images(paths, clean_message, pasted_images).await
    };
    drain_stdin();
    match result {
        // Ctrl+C 不是故障：暗一行「已取消」就够了，别顶着红色的「错误」。
        Err(err)
            if err
                .downcast_ref::<crate::cli::repl::session::RemoteTurnCancelled>()
                .is_some() =>
        {
            println!("\x1b[2m{}\x1b[0m", t("cancelled", "已取消"));
            Ok(())
        }
        // 其余错误这里不打印：往上返回后 `main.rs` 会打一次。以前这里先打
        // 一遍再返回 Err，同一句「错误: …」就会出现两次。
        other => other,
    }
}

pub(in crate::cli) fn expand_shell_pasted_text_placeholders(
    paths: &MiyuPaths,
    message: &str,
) -> Result<String> {
    let placeholders = find_pasted_text_placeholders(message);
    if placeholders.is_empty() {
        return Ok(message.to_string());
    }

    let chars: Vec<char> = message.chars().collect();
    let mut expanded = String::new();
    let mut last_end = 0;
    let dir = paths.cache_dir.join("clipboard_texts");
    for (start, end, index) in placeholders {
        expanded.extend(&chars[last_end..start]);
        let path = dir.join(format!("{index}.txt"));
        match std::fs::read_to_string(&path) {
            Ok(text) => expanded.push_str(&text),
            Err(_) => expanded.extend(&chars[start..end]),
        }
        last_end = end;
    }
    expanded.extend(&chars[last_end..]);
    Ok(expanded)
}

#[cfg(test)]
mod short_link_tests {
    use super::*;

    /// 短链软链:32 位哈希名得到 8 位短名软链且指向原文件;重复调用幂等;
    /// 本来就短的名字原样返回不建链。
    #[test]
    fn short_image_link_creates_idempotent_symlink() {
        let temp = tempfile::tempdir().unwrap();
        let filename = "552921ce0e9994cb6d412899365c87a1.png";
        let path = temp.path().join(filename);
        std::fs::write(&path, b"png").unwrap();
        let short = short_image_link(&path, filename).unwrap();
        assert_eq!(short, "552921ce.png");
        let link = temp.path().join(&short);
        assert_eq!(std::fs::read(&link).unwrap(), b"png");
        // 幂等:再来一次不报错、还指向同处。
        assert_eq!(short_image_link(&path, filename).unwrap(), "552921ce.png");
        // 短名原样返回。
        let short_file = temp.path().join("cat.png");
        std::fs::write(&short_file, b"x").unwrap();
        assert_eq!(short_image_link(&short_file, "cat.png").unwrap(), "cat.png");
    }
}
