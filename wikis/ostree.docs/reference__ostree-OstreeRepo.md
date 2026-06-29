[TABLE]

## Functions

|  |  |
|----|----|
| gboolean | [ostree_repo_mode_from_string](reference__ostree-OstreeRepo.md#ostree-repo-mode-from-string "ostree_repo_mode_from_string ()") () |
| [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") \* | [ostree_repo_open_at](reference__ostree-OstreeRepo.md#ostree-repo-open-at "ostree_repo_open_at ()") () |
| [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") \* | [ostree_repo_new](reference__ostree-OstreeRepo.md#ostree-repo-new "ostree_repo_new ()") () |
| [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") \* | [ostree_repo_new_for_sysroot_path](reference__ostree-OstreeRepo.md#ostree-repo-new-for-sysroot-path "ostree_repo_new_for_sysroot_path ()") () |
| [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") \* | [ostree_repo_new_default](reference__ostree-OstreeRepo.md#ostree-repo-new-default "ostree_repo_new_default ()") () |
| gboolean | [ostree_repo_open](reference__ostree-OstreeRepo.md#ostree-repo-open "ostree_repo_open ()") () |
| void | [ostree_repo_set_disable_fsync](reference__ostree-OstreeRepo.md#ostree-repo-set-disable-fsync "ostree_repo_set_disable_fsync ()") () |
| gboolean | [ostree_repo_get_disable_fsync](reference__ostree-OstreeRepo.md#ostree-repo-get-disable-fsync "ostree_repo_get_disable_fsync ()") () |
| gboolean | [ostree_repo_is_system](reference__ostree-OstreeRepo.md#ostree-repo-is-system "ostree_repo_is_system ()") () |
| gboolean | [ostree_repo_is_writable](reference__ostree-OstreeRepo.md#ostree-repo-is-writable "ostree_repo_is_writable ()") () |
| [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") \* | [ostree_repo_create_at](reference__ostree-OstreeRepo.md#ostree-repo-create-at "ostree_repo_create_at ()") () |
| gboolean | [ostree_repo_create](reference__ostree-OstreeRepo.md#ostree-repo-create "ostree_repo_create ()") () |
| const gchar \* | [ostree_repo_get_collection_id](reference__ostree-OstreeRepo.md#ostree-repo-get-collection-id "ostree_repo_get_collection_id ()") () |
| const gchar \* | [ostree_repo_get_bootloader](reference__ostree-OstreeRepo.md#ostree-repo-get-bootloader "ostree_repo_get_bootloader ()") () |
| GFile \* | [ostree_repo_get_path](reference__ostree-OstreeRepo.md#ostree-repo-get-path "ostree_repo_get_path ()") () |
| [OstreeRepoMode](reference__ostree-OstreeRepo.md#OstreeRepoMode "enum OstreeRepoMode") | [ostree_repo_get_mode](reference__ostree-OstreeRepo.md#ostree-repo-get-mode "ostree_repo_get_mode ()") () |
| gboolean | [ostree_repo_get_min_free_space_bytes](reference__ostree-OstreeRepo.md#ostree-repo-get-min-free-space-bytes "ostree_repo_get_min_free_space_bytes ()") () |
| GKeyFile \* | [ostree_repo_get_config](reference__ostree-OstreeRepo.md#ostree-repo-get-config "ostree_repo_get_config ()") () |
| int | [ostree_repo_get_dfd](reference__ostree-OstreeRepo.md#ostree-repo-get-dfd "ostree_repo_get_dfd ()") () |
| const gchar \*const \* | [ostree_repo_get_default_repo_finders](reference__ostree-OstreeRepo.md#ostree-repo-get-default-repo-finders "ostree_repo_get_default_repo_finders ()") () |
| gboolean | [ostree_repo_lock_pop](reference__ostree-OstreeRepo.md#ostree-repo-lock-pop "ostree_repo_lock_pop ()") () |
| gboolean | [ostree_repo_lock_push](reference__ostree-OstreeRepo.md#ostree-repo-lock-push "ostree_repo_lock_push ()") () |
| [OstreeRepoAutoLock](reference__ostree-OstreeRepo.md#OstreeRepoAutoLock "OstreeRepoAutoLock") \* | [ostree_repo_auto_lock_push](reference__ostree-OstreeRepo.md#ostree-repo-auto-lock-push "ostree_repo_auto_lock_push ()") () |
| void | [ostree_repo_auto_lock_cleanup](reference__ostree-OstreeRepo.md#ostree-repo-auto-lock-cleanup "ostree_repo_auto_lock_cleanup ()") () |
| guint | [ostree_repo_hash](reference__ostree-OstreeRepo.md#ostree-repo-hash "ostree_repo_hash ()") () |
| gboolean | [ostree_repo_equal](reference__ostree-OstreeRepo.md#ostree-repo-equal "ostree_repo_equal ()") () |
| GKeyFile \* | [ostree_repo_copy_config](reference__ostree-OstreeRepo.md#ostree-repo-copy-config "ostree_repo_copy_config ()") () |
| gboolean | [ostree_repo_remote_add](reference__ostree-OstreeRepo.md#ostree-repo-remote-add "ostree_repo_remote_add ()") () |
| gboolean | [ostree_repo_remote_delete](reference__ostree-OstreeRepo.md#ostree-repo-remote-delete "ostree_repo_remote_delete ()") () |
| gboolean | [ostree_repo_remote_change](reference__ostree-OstreeRepo.md#ostree-repo-remote-change "ostree_repo_remote_change ()") () |
| char \*\* | [ostree_repo_remote_list](reference__ostree-OstreeRepo.md#ostree-repo-remote-list "ostree_repo_remote_list ()") () |
| gboolean | [ostree_repo_remote_list_collection_refs](reference__ostree-OstreeRepo.md#ostree-repo-remote-list-collection-refs "ostree_repo_remote_list_collection_refs ()") () |
| gboolean | [ostree_repo_remote_get_url](reference__ostree-OstreeRepo.md#ostree-repo-remote-get-url "ostree_repo_remote_get_url ()") () |
| gboolean | [ostree_repo_remote_get_gpg_verify](reference__ostree-OstreeRepo.md#ostree-repo-remote-get-gpg-verify "ostree_repo_remote_get_gpg_verify ()") () |
| gboolean | [ostree_repo_remote_get_gpg_verify_summary](reference__ostree-OstreeRepo.md#ostree-repo-remote-get-gpg-verify-summary "ostree_repo_remote_get_gpg_verify_summary ()") () |
| gboolean | [ostree_repo_remote_get_gpg_keys](reference__ostree-OstreeRepo.md#ostree-repo-remote-get-gpg-keys "ostree_repo_remote_get_gpg_keys ()") () |
| gboolean | [ostree_repo_remote_gpg_import](reference__ostree-OstreeRepo.md#ostree-repo-remote-gpg-import "ostree_repo_remote_gpg_import ()") () |
| gboolean | [ostree_repo_remote_fetch_summary](reference__ostree-OstreeRepo.md#ostree-repo-remote-fetch-summary "ostree_repo_remote_fetch_summary ()") () |
| gboolean | [ostree_repo_remote_fetch_summary_with_options](reference__ostree-OstreeRepo.md#ostree-repo-remote-fetch-summary-with-options "ostree_repo_remote_fetch_summary_with_options ()") () |
| gboolean | [ostree_repo_reload_config](reference__ostree-OstreeRepo.md#ostree-repo-reload-config "ostree_repo_reload_config ()") () |
| gboolean | [ostree_repo_get_remote_boolean_option](reference__ostree-OstreeRepo.md#ostree-repo-get-remote-boolean-option "ostree_repo_get_remote_boolean_option ()") () |
| gboolean | [ostree_repo_get_remote_list_option](reference__ostree-OstreeRepo.md#ostree-repo-get-remote-list-option "ostree_repo_get_remote_list_option ()") () |
| gboolean | [ostree_repo_get_remote_option](reference__ostree-OstreeRepo.md#ostree-repo-get-remote-option "ostree_repo_get_remote_option ()") () |
| [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") \* | [ostree_repo_get_parent](reference__ostree-OstreeRepo.md#ostree-repo-get-parent "ostree_repo_get_parent ()") () |
| gboolean | [ostree_repo_write_config](reference__ostree-OstreeRepo.md#ostree-repo-write-config "ostree_repo_write_config ()") () |
| gboolean | [ostree_repo_write_config_and_reload](reference__ostree-OstreeRepo.md#ostree-repo-write-config-and-reload "ostree_repo_write_config_and_reload ()") () |
| gboolean | [ostree_repo_scan_hardlinks](reference__ostree-OstreeRepo.md#ostree-repo-scan-hardlinks "ostree_repo_scan_hardlinks ()") () |
| gboolean | [ostree_repo_prepare_transaction](reference__ostree-OstreeRepo.md#ostree-repo-prepare-transaction "ostree_repo_prepare_transaction ()") () |
| gboolean | [ostree_repo_commit_transaction](reference__ostree-OstreeRepo.md#ostree-repo-commit-transaction "ostree_repo_commit_transaction ()") () |
| gboolean | [ostree_repo_abort_transaction](reference__ostree-OstreeRepo.md#ostree-repo-abort-transaction "ostree_repo_abort_transaction ()") () |
| void | [ostree_repo_transaction_set_refspec](reference__ostree-OstreeRepo.md#ostree-repo-transaction-set-refspec "ostree_repo_transaction_set_refspec ()") () |
| void | [ostree_repo_transaction_set_collection_ref](reference__ostree-OstreeRepo.md#ostree-repo-transaction-set-collection-ref "ostree_repo_transaction_set_collection_ref ()") () |
| void | [ostree_repo_transaction_set_ref](reference__ostree-OstreeRepo.md#ostree-repo-transaction-set-ref "ostree_repo_transaction_set_ref ()") () |
| gboolean | [ostree_repo_set_ref_immediate](reference__ostree-OstreeRepo.md#ostree-repo-set-ref-immediate "ostree_repo_set_ref_immediate ()") () |
| gboolean | [ostree_repo_set_alias_ref_immediate](reference__ostree-OstreeRepo.md#ostree-repo-set-alias-ref-immediate "ostree_repo_set_alias_ref_immediate ()") () |
| gboolean | [ostree_repo_set_cache_dir](reference__ostree-OstreeRepo.md#ostree-repo-set-cache-dir "ostree_repo_set_cache_dir ()") () |
| gboolean | [ostree_repo_set_collection_id](reference__ostree-OstreeRepo.md#ostree-repo-set-collection-id "ostree_repo_set_collection_id ()") () |
| gboolean | [ostree_repo_set_collection_ref_immediate](reference__ostree-OstreeRepo.md#ostree-repo-set-collection-ref-immediate "ostree_repo_set_collection_ref_immediate ()") () |
| gboolean | [ostree_repo_sign_delta](reference__ostree-OstreeRepo.md#ostree-repo-sign-delta "ostree_repo_sign_delta ()") () |
| gboolean | [ostree_repo_has_object](reference__ostree-OstreeRepo.md#ostree-repo-has-object "ostree_repo_has_object ()") () |
| gboolean | [ostree_repo_mark_commit_partial](reference__ostree-OstreeRepo.md#ostree-repo-mark-commit-partial "ostree_repo_mark_commit_partial ()") () |
| gboolean | [ostree_repo_mark_commit_partial_reason](reference__ostree-OstreeRepo.md#ostree-repo-mark-commit-partial-reason "ostree_repo_mark_commit_partial_reason ()") () |
| gboolean | [ostree_repo_write_metadata](reference__ostree-OstreeRepo.md#ostree-repo-write-metadata "ostree_repo_write_metadata ()") () |
| void | [ostree_repo_write_metadata_async](reference__ostree-OstreeRepo.md#ostree-repo-write-metadata-async "ostree_repo_write_metadata_async ()") () |
| gboolean | [ostree_repo_write_metadata_finish](reference__ostree-OstreeRepo.md#ostree-repo-write-metadata-finish "ostree_repo_write_metadata_finish ()") () |
| gboolean | [ostree_repo_write_content](reference__ostree-OstreeRepo.md#ostree-repo-write-content "ostree_repo_write_content ()") () |
| OstreeContentWriter \* | [ostree_repo_write_regfile](reference__ostree-OstreeRepo.md#ostree-repo-write-regfile "ostree_repo_write_regfile ()") () |
| char \* | [ostree_repo_write_regfile_inline](reference__ostree-OstreeRepo.md#ostree-repo-write-regfile-inline "ostree_repo_write_regfile_inline ()") () |
| char \* | [ostree_repo_write_symlink](reference__ostree-OstreeRepo.md#ostree-repo-write-symlink "ostree_repo_write_symlink ()") () |
| gboolean | [ostree_repo_write_metadata_trusted](reference__ostree-OstreeRepo.md#ostree-repo-write-metadata-trusted "ostree_repo_write_metadata_trusted ()") () |
| gboolean | [ostree_repo_write_metadata_stream_trusted](reference__ostree-OstreeRepo.md#ostree-repo-write-metadata-stream-trusted "ostree_repo_write_metadata_stream_trusted ()") () |
| gboolean | [ostree_repo_write_content_trusted](reference__ostree-OstreeRepo.md#ostree-repo-write-content-trusted "ostree_repo_write_content_trusted ()") () |
| void | [ostree_repo_write_content_async](reference__ostree-OstreeRepo.md#ostree-repo-write-content-async "ostree_repo_write_content_async ()") () |
| gboolean | [ostree_repo_write_content_finish](reference__ostree-OstreeRepo.md#ostree-repo-write-content-finish "ostree_repo_write_content_finish ()") () |
| gboolean | [ostree_repo_resolve_rev](reference__ostree-OstreeRepo.md#ostree-repo-resolve-rev "ostree_repo_resolve_rev ()") () |
| gboolean | [ostree_repo_resolve_rev_ext](reference__ostree-OstreeRepo.md#ostree-repo-resolve-rev-ext "ostree_repo_resolve_rev_ext ()") () |
| gboolean | [ostree_repo_list_refs](reference__ostree-OstreeRepo.md#ostree-repo-list-refs "ostree_repo_list_refs ()") () |
| gboolean | [ostree_repo_list_refs_ext](reference__ostree-OstreeRepo.md#ostree-repo-list-refs-ext "ostree_repo_list_refs_ext ()") () |
| gboolean | [ostree_repo_list_collection_refs](reference__ostree-OstreeRepo.md#ostree-repo-list-collection-refs "ostree_repo_list_collection_refs ()") () |
| gboolean | [ostree_repo_remote_list_refs](reference__ostree-OstreeRepo.md#ostree-repo-remote-list-refs "ostree_repo_remote_list_refs ()") () |
| gboolean | [ostree_repo_resolve_collection_ref](reference__ostree-OstreeRepo.md#ostree-repo-resolve-collection-ref "ostree_repo_resolve_collection_ref ()") () |
| gboolean | [ostree_repo_load_variant](reference__ostree-OstreeRepo.md#ostree-repo-load-variant "ostree_repo_load_variant ()") () |
| gboolean | [ostree_repo_load_commit](reference__ostree-OstreeRepo.md#ostree-repo-load-commit "ostree_repo_load_commit ()") () |
| gboolean | [ostree_repo_load_variant_if_exists](reference__ostree-OstreeRepo.md#ostree-repo-load-variant-if-exists "ostree_repo_load_variant_if_exists ()") () |
| gboolean | [ostree_repo_load_file](reference__ostree-OstreeRepo.md#ostree-repo-load-file "ostree_repo_load_file ()") () |
| gboolean | [ostree_repo_load_object_stream](reference__ostree-OstreeRepo.md#ostree-repo-load-object-stream "ostree_repo_load_object_stream ()") () |
| gboolean | [ostree_repo_query_object_storage_size](reference__ostree-OstreeRepo.md#ostree-repo-query-object-storage-size "ostree_repo_query_object_storage_size ()") () |
| gboolean | [ostree_repo_import_object_from](reference__ostree-OstreeRepo.md#ostree-repo-import-object-from "ostree_repo_import_object_from ()") () |
| gboolean | [ostree_repo_import_object_from_with_trust](reference__ostree-OstreeRepo.md#ostree-repo-import-object-from-with-trust "ostree_repo_import_object_from_with_trust ()") () |
| gboolean | [ostree_repo_import_archive_to_mtree](reference__ostree-OstreeRepo.md#ostree-repo-import-archive-to-mtree "ostree_repo_import_archive_to_mtree ()") () |
| gboolean | [ostree_repo_export_tree_to_archive](reference__ostree-OstreeRepo.md#ostree-repo-export-tree-to-archive "ostree_repo_export_tree_to_archive ()") () |
| gboolean | [ostree_repo_delete_object](reference__ostree-OstreeRepo.md#ostree-repo-delete-object "ostree_repo_delete_object ()") () |
| gboolean | [ostree_repo_fsck_object](reference__ostree-OstreeRepo.md#ostree-repo-fsck-object "ostree_repo_fsck_object ()") () |
| [OstreeRepoCommitFilterResult](reference__ostree-OstreeRepo.md#OstreeRepoCommitFilterResult "enum OstreeRepoCommitFilterResult") | ([\*OstreeRepoCommitFilter](reference__ostree-OstreeRepo.md#OstreeRepoCommitFilter "OstreeRepoCommitFilter ()")) () |
| [OstreeRepoCommitModifier](reference__ostree-OstreeRepo.md#OstreeRepoCommitModifier "OstreeRepoCommitModifier") \* | [ostree_repo_commit_modifier_new](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-new "ostree_repo_commit_modifier_new ()") () |
| GVariant \* | ([\*OstreeRepoCommitModifierXattrCallback](reference__ostree-OstreeRepo.md#OstreeRepoCommitModifierXattrCallback "OstreeRepoCommitModifierXattrCallback ()")) () |
| void | [ostree_repo_commit_modifier_set_xattr_callback](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-set-xattr-callback "ostree_repo_commit_modifier_set_xattr_callback ()") () |
| void | [ostree_repo_commit_modifier_set_sepolicy](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-set-sepolicy "ostree_repo_commit_modifier_set_sepolicy ()") () |
| gboolean | [ostree_repo_commit_modifier_set_sepolicy_from_commit](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-set-sepolicy-from-commit "ostree_repo_commit_modifier_set_sepolicy_from_commit ()") () |
| void | [ostree_repo_commit_modifier_set_devino_cache](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-set-devino-cache "ostree_repo_commit_modifier_set_devino_cache ()") () |
| [OstreeRepoCommitModifier](reference__ostree-OstreeRepo.md#OstreeRepoCommitModifier "OstreeRepoCommitModifier") \* | [ostree_repo_commit_modifier_ref](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-ref "ostree_repo_commit_modifier_ref ()") () |
| void | [ostree_repo_commit_modifier_unref](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-unref "ostree_repo_commit_modifier_unref ()") () |
| OstreeRepoDevInoCache \* | [ostree_repo_devino_cache_new](reference__ostree-OstreeRepo.md#ostree-repo-devino-cache-new "ostree_repo_devino_cache_new ()") () |
| OstreeRepoDevInoCache \* | [ostree_repo_devino_cache_ref](reference__ostree-OstreeRepo.md#ostree-repo-devino-cache-ref "ostree_repo_devino_cache_ref ()") () |
| void | [ostree_repo_devino_cache_unref](reference__ostree-OstreeRepo.md#ostree-repo-devino-cache-unref "ostree_repo_devino_cache_unref ()") () |
| GType | [ostree_repo_devino_cache_get_type](reference__ostree-OstreeRepo.md#ostree-repo-devino-cache-get-type "ostree_repo_devino_cache_get_type ()") () |
| gboolean | [ostree_repo_write_directory_to_mtree](reference__ostree-OstreeRepo.md#ostree-repo-write-directory-to-mtree "ostree_repo_write_directory_to_mtree ()") () |
| gboolean | [ostree_repo_write_dfd_to_mtree](reference__ostree-OstreeRepo.md#ostree-repo-write-dfd-to-mtree "ostree_repo_write_dfd_to_mtree ()") () |
| gboolean | [ostree_repo_write_archive_to_mtree](reference__ostree-OstreeRepo.md#ostree-repo-write-archive-to-mtree "ostree_repo_write_archive_to_mtree ()") () |
| gboolean | [ostree_repo_write_archive_to_mtree_from_fd](reference__ostree-OstreeRepo.md#ostree-repo-write-archive-to-mtree-from-fd "ostree_repo_write_archive_to_mtree_from_fd ()") () |
| gboolean | [ostree_repo_write_mtree](reference__ostree-OstreeRepo.md#ostree-repo-write-mtree "ostree_repo_write_mtree ()") () |
| gboolean | [ostree_repo_write_commit](reference__ostree-OstreeRepo.md#ostree-repo-write-commit "ostree_repo_write_commit ()") () |
| gboolean | [ostree_repo_write_commit_with_time](reference__ostree-OstreeRepo.md#ostree-repo-write-commit-with-time "ostree_repo_write_commit_with_time ()") () |
| gboolean | [ostree_repo_read_commit_detached_metadata](reference__ostree-OstreeRepo.md#ostree-repo-read-commit-detached-metadata "ostree_repo_read_commit_detached_metadata ()") () |
| gboolean | [ostree_repo_write_commit_detached_metadata](reference__ostree-OstreeRepo.md#ostree-repo-write-commit-detached-metadata "ostree_repo_write_commit_detached_metadata ()") () |
| gboolean | [ostree_repo_commit_add_composefs_metadata](reference__ostree-OstreeRepo.md#ostree-repo-commit-add-composefs-metadata "ostree_repo_commit_add_composefs_metadata ()") () |
| void | [ostree_repo_checkout_at_options_set_devino](reference__ostree-OstreeRepo.md#ostree-repo-checkout-at-options-set-devino "ostree_repo_checkout_at_options_set_devino ()") () |
| gboolean | [ostree_repo_checkout_tree](reference__ostree-OstreeRepo.md#ostree-repo-checkout-tree "ostree_repo_checkout_tree ()") () |
| gboolean | [ostree_repo_checkout_tree_at](reference__ostree-OstreeRepo.md#ostree-repo-checkout-tree-at "ostree_repo_checkout_tree_at ()") () |
| gboolean | [ostree_repo_checkout_at](reference__ostree-OstreeRepo.md#ostree-repo-checkout-at "ostree_repo_checkout_at ()") () |
| gboolean | [ostree_repo_checkout_composefs](reference__ostree-OstreeRepo.md#ostree-repo-checkout-composefs "ostree_repo_checkout_composefs ()") () |
| gboolean | [ostree_repo_checkout_gc](reference__ostree-OstreeRepo.md#ostree-repo-checkout-gc "ostree_repo_checkout_gc ()") () |
| gboolean | [ostree_repo_read_commit](reference__ostree-OstreeRepo.md#ostree-repo-read-commit "ostree_repo_read_commit ()") () |
| gboolean | [ostree_repo_list_objects](reference__ostree-OstreeRepo.md#ostree-repo-list-objects "ostree_repo_list_objects ()") () |
| gboolean | [ostree_repo_list_commit_objects_starting_with](reference__ostree-OstreeRepo.md#ostree-repo-list-commit-objects-starting-with "ostree_repo_list_commit_objects_starting_with ()") () |
| gboolean | [ostree_repo_list_static_delta_names](reference__ostree-OstreeRepo.md#ostree-repo-list-static-delta-names "ostree_repo_list_static_delta_names ()") () |
| gboolean | [ostree_repo_list_static_delta_indexes](reference__ostree-OstreeRepo.md#ostree-repo-list-static-delta-indexes "ostree_repo_list_static_delta_indexes ()") () |
| gboolean | [ostree_repo_static_delta_reindex](reference__ostree-OstreeRepo.md#ostree-repo-static-delta-reindex "ostree_repo_static_delta_reindex ()") () |
| gboolean | [ostree_repo_static_delta_generate](reference__ostree-OstreeRepo.md#ostree-repo-static-delta-generate "ostree_repo_static_delta_generate ()") () |
| gboolean | [ostree_repo_static_delta_execute_offline_with_signature](reference__ostree-OstreeRepo.md#ostree-repo-static-delta-execute-offline-with-signature "ostree_repo_static_delta_execute_offline_with_signature ()") () |
| gboolean | [ostree_repo_static_delta_execute_offline](reference__ostree-OstreeRepo.md#ostree-repo-static-delta-execute-offline "ostree_repo_static_delta_execute_offline ()") () |
| gboolean | [ostree_repo_static_delta_verify_signature](reference__ostree-OstreeRepo.md#ostree-repo-static-delta-verify-signature "ostree_repo_static_delta_verify_signature ()") () |
| GHashTable \* | [ostree_repo_traverse_new_reachable](reference__ostree-OstreeRepo.md#ostree-repo-traverse-new-reachable "ostree_repo_traverse_new_reachable ()") () |
| GHashTable \* | [ostree_repo_traverse_new_parents](reference__ostree-OstreeRepo.md#ostree-repo-traverse-new-parents "ostree_repo_traverse_new_parents ()") () |
| char \*\* | [ostree_repo_traverse_parents_get_commits](reference__ostree-OstreeRepo.md#ostree-repo-traverse-parents-get-commits "ostree_repo_traverse_parents_get_commits ()") () |
| gboolean | [ostree_repo_traverse_commit](reference__ostree-OstreeRepo.md#ostree-repo-traverse-commit "ostree_repo_traverse_commit ()") () |
| gboolean | [ostree_repo_traverse_commit_union](reference__ostree-OstreeRepo.md#ostree-repo-traverse-commit-union "ostree_repo_traverse_commit_union ()") () |
| gboolean | [ostree_repo_traverse_commit_union_with_parents](reference__ostree-OstreeRepo.md#ostree-repo-traverse-commit-union-with-parents "ostree_repo_traverse_commit_union_with_parents ()") () |
| gboolean | [ostree_repo_traverse_commit_with_flags](reference__ostree-OstreeRepo.md#ostree-repo-traverse-commit-with-flags "ostree_repo_traverse_commit_with_flags ()") () |
| void | [ostree_repo_commit_traverse_iter_cleanup](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-cleanup "ostree_repo_commit_traverse_iter_cleanup ()") () |
| void | [ostree_repo_commit_traverse_iter_clear](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-clear "ostree_repo_commit_traverse_iter_clear ()") () |
| void | [ostree_repo_commit_traverse_iter_get_dir](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-get-dir "ostree_repo_commit_traverse_iter_get_dir ()") () |
| void | [ostree_repo_commit_traverse_iter_get_file](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-get-file "ostree_repo_commit_traverse_iter_get_file ()") () |
| gboolean | [ostree_repo_commit_traverse_iter_init_commit](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-init-commit "ostree_repo_commit_traverse_iter_init_commit ()") () |
| gboolean | [ostree_repo_commit_traverse_iter_init_dirtree](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-init-dirtree "ostree_repo_commit_traverse_iter_init_dirtree ()") () |
| [OstreeRepoCommitIterResult](reference__ostree-OstreeRepo.md#OstreeRepoCommitIterResult "enum OstreeRepoCommitIterResult") | [ostree_repo_commit_traverse_iter_next](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-next "ostree_repo_commit_traverse_iter_next ()") () |
| gboolean | [ostree_repo_prune](reference__ostree-OstreeRepo.md#ostree-repo-prune "ostree_repo_prune ()") () |
| gboolean | [ostree_repo_prune_static_deltas](reference__ostree-OstreeRepo.md#ostree-repo-prune-static-deltas "ostree_repo_prune_static_deltas ()") () |
| gboolean | [ostree_repo_traverse_reachable_refs](reference__ostree-OstreeRepo.md#ostree-repo-traverse-reachable-refs "ostree_repo_traverse_reachable_refs ()") () |
| gboolean | [ostree_repo_prune_from_reachable](reference__ostree-OstreeRepo.md#ostree-repo-prune-from-reachable "ostree_repo_prune_from_reachable ()") () |
| gboolean | [ostree_repo_pull](reference__ostree-OstreeRepo.md#ostree-repo-pull "ostree_repo_pull ()") () |
| gboolean | [ostree_repo_pull_one_dir](reference__ostree-OstreeRepo.md#ostree-repo-pull-one-dir "ostree_repo_pull_one_dir ()") () |
| gboolean | [ostree_repo_pull_with_options](reference__ostree-OstreeRepo.md#ostree-repo-pull-with-options "ostree_repo_pull_with_options ()") () |
| void | [ostree_repo_pull_default_console_progress_changed](reference__ostree-OstreeRepo.md#ostree-repo-pull-default-console-progress-changed "ostree_repo_pull_default_console_progress_changed ()") () |
| gboolean | [ostree_repo_sign_commit](reference__ostree-OstreeRepo.md#ostree-repo-sign-commit "ostree_repo_sign_commit ()") () |
| gboolean | [ostree_repo_append_gpg_signature](reference__ostree-OstreeRepo.md#ostree-repo-append-gpg-signature "ostree_repo_append_gpg_signature ()") () |
| gboolean | [ostree_repo_add_gpg_signature_summary](reference__ostree-OstreeRepo.md#ostree-repo-add-gpg-signature-summary "ostree_repo_add_gpg_signature_summary ()") () |
| gboolean | [ostree_repo_gpg_sign_data](reference__ostree-OstreeRepo.md#ostree-repo-gpg-sign-data "ostree_repo_gpg_sign_data ()") () |
| [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") \* | [ostree_repo_gpg_verify_data](reference__ostree-OstreeRepo.md#ostree-repo-gpg-verify-data "ostree_repo_gpg_verify_data ()") () |
| gboolean | [ostree_repo_signature_verify_commit_data](reference__ostree-OstreeRepo.md#ostree-repo-signature-verify-commit-data "ostree_repo_signature_verify_commit_data ()") () |
| gboolean | [ostree_repo_verify_commit](reference__ostree-OstreeRepo.md#ostree-repo-verify-commit "ostree_repo_verify_commit ()") () |
| [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") \* | [ostree_repo_verify_commit_ext](reference__ostree-OstreeRepo.md#ostree-repo-verify-commit-ext "ostree_repo_verify_commit_ext ()") () |
| [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") \* | [ostree_repo_verify_commit_for_remote](reference__ostree-OstreeRepo.md#ostree-repo-verify-commit-for-remote "ostree_repo_verify_commit_for_remote ()") () |
| [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") \* | [ostree_repo_verify_summary](reference__ostree-OstreeRepo.md#ostree-repo-verify-summary "ostree_repo_verify_summary ()") () |
| gboolean | [ostree_repo_regenerate_metadata](reference__ostree-OstreeRepo.md#ostree-repo-regenerate-metadata "ostree_repo_regenerate_metadata ()") () |
| gboolean | [ostree_repo_regenerate_summary](reference__ostree-OstreeRepo.md#ostree-repo-regenerate-summary "ostree_repo_regenerate_summary ()") () |

## Types and Values

|  |  |
|----|----|
| typedef | [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |
| enum | [OstreeRepoMode](reference__ostree-OstreeRepo.md#OstreeRepoMode "enum OstreeRepoMode") |
| enum | [OstreeRepoLockType](reference__ostree-OstreeRepo.md#OstreeRepoLockType "enum OstreeRepoLockType") |
| typedef | [OstreeRepoAutoLock](reference__ostree-OstreeRepo.md#OstreeRepoAutoLock "OstreeRepoAutoLock") |
| enum | [OstreeRepoRemoteChange](reference__ostree-OstreeRepo.md#OstreeRepoRemoteChange "enum OstreeRepoRemoteChange") |
| struct | [OstreeRepoTransactionStats](reference__ostree-OstreeRepo.md#OstreeRepoTransactionStats "struct OstreeRepoTransactionStats") |
| enum | [OstreeRepoResolveRevExtFlags](reference__ostree-OstreeRepo.md#OstreeRepoResolveRevExtFlags "enum OstreeRepoResolveRevExtFlags") |
| enum | [OstreeRepoListRefsExtFlags](reference__ostree-OstreeRepo.md#OstreeRepoListRefsExtFlags "enum OstreeRepoListRefsExtFlags") |
| enum | [OstreeRepoCommitState](reference__ostree-OstreeRepo.md#OstreeRepoCommitState "enum OstreeRepoCommitState") |
| enum | [OstreeRepoCommitFilterResult](reference__ostree-OstreeRepo.md#OstreeRepoCommitFilterResult "enum OstreeRepoCommitFilterResult") |
| typedef | [OstreeRepoCommitModifier](reference__ostree-OstreeRepo.md#OstreeRepoCommitModifier "OstreeRepoCommitModifier") |
| enum | [OstreeRepoCommitModifierFlags](reference__ostree-OstreeRepo.md#OstreeRepoCommitModifierFlags "enum OstreeRepoCommitModifierFlags") |
| enum | [OstreeRepoCheckoutMode](reference__ostree-OstreeRepo.md#OstreeRepoCheckoutMode "enum OstreeRepoCheckoutMode") |
| enum | [OstreeRepoCheckoutOverwriteMode](reference__ostree-OstreeRepo.md#OstreeRepoCheckoutOverwriteMode "enum OstreeRepoCheckoutOverwriteMode") |
| enum | [OstreeRepoListObjectsFlags](reference__ostree-OstreeRepo.md#OstreeRepoListObjectsFlags "enum OstreeRepoListObjectsFlags") |
| \#define | [OSTREE_REPO_LIST_OBJECTS_VARIANT_TYPE](reference__ostree-OstreeRepo.md#OSTREE-REPO-LIST-OBJECTS-VARIANT-TYPE:CAPS "OSTREE_REPO_LIST_OBJECTS_VARIANT_TYPE") |
| enum | [OstreeStaticDeltaGenerateOpt](reference__ostree-OstreeRepo.md#OstreeStaticDeltaGenerateOpt "enum OstreeStaticDeltaGenerateOpt") |
| enum | [OstreeRepoCommitTraverseFlags](reference__ostree-OstreeRepo.md#OstreeRepoCommitTraverseFlags "enum OstreeRepoCommitTraverseFlags") |
| enum | [OstreeRepoCommitIterResult](reference__ostree-OstreeRepo.md#OstreeRepoCommitIterResult "enum OstreeRepoCommitIterResult") |
| enum | [OstreeRepoPruneFlags](reference__ostree-OstreeRepo.md#OstreeRepoPruneFlags "enum OstreeRepoPruneFlags") |
| enum | [OstreeRepoPullFlags](reference__ostree-OstreeRepo.md#OstreeRepoPullFlags "enum OstreeRepoPullFlags") |

## Description

The [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") is like git, a content-addressed object store. Unlike git, it records uid, gid, and extended attributes.

There are four possible "modes" for an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo"); [`OSTREE_REPO_MODE_BARE`](reference__ostree-OstreeRepo.md#OSTREE-REPO-MODE-BARE:CAPS) is very simple - content files are represented exactly as they are, and checkouts are just hardlinks. [`OSTREE_REPO_MODE_BARE_USER`](reference__ostree-OstreeRepo.md#OSTREE-REPO-MODE-BARE-USER:CAPS) is similar, except the uid/gids are not set on the files, and checkouts as hardlinks work only for user checkouts. [`OSTREE_REPO_MODE_BARE_USER_ONLY`](reference__ostree-OstreeRepo.md#OSTREE-REPO-MODE-BARE-USER-ONLY:CAPS) is the same as BARE_USER, but all metadata is not stored, so it can only be used for user checkouts. This mode does not require xattrs. A [`OSTREE_REPO_MODE_ARCHIVE`](reference__ostree-OstreeRepo.md#OSTREE-REPO-MODE-ARCHIVE:CAPS) (also known as [`OSTREE_REPO_MODE_ARCHIVE_Z2`](reference__ostree-OstreeRepo.md#OSTREE-REPO-MODE-ARCHIVE-Z2:CAPS)) repository in contrast stores content files zlib-compressed. It is suitable for non-root-owned repositories that can be served via a static HTTP server.

Creating an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") does not invoke any file I/O, and thus needs to be initialized, either from existing contents or as a new repository. If you have an existing repo, use [`ostree_repo_open()`](reference__ostree-OstreeRepo.md#ostree-repo-open "ostree_repo_open ()") to load it from disk and check its validity. To initialize a new repository in the given filepath, use [`ostree_repo_create()`](reference__ostree-OstreeRepo.md#ostree-repo-create "ostree_repo_create ()") instead.

To store content in the repo, first start a transaction with [`ostree_repo_prepare_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-prepare-transaction "ostree_repo_prepare_transaction ()"). Then create a [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree"), and apply functions such as [`ostree_repo_write_directory_to_mtree()`](reference__ostree-OstreeRepo.md#ostree-repo-write-directory-to-mtree "ostree_repo_write_directory_to_mtree ()") to traverse a physical filesystem and write content, possibly multiple times.

Once the [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") is complete, write all of its metadata with [`ostree_repo_write_mtree()`](reference__ostree-OstreeRepo.md#ostree-repo-write-mtree "ostree_repo_write_mtree ()"), and finally create a commit with [`ostree_repo_write_commit()`](reference__ostree-OstreeRepo.md#ostree-repo-write-commit "ostree_repo_write_commit ()").

#### Collection IDs

A collection ID is a globally unique identifier which, if set, is used to identify refs from a repository which are mirrored elsewhere, such as in mirror repositories or peer to peer networks.

This is separate from the `collection-id` configuration key for a remote, which is used to store the collection ID of the repository that remote points to.

The collection ID should only be set on an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") if it is the canonical collection for some refs.

A collection ID must be a reverse DNS name, where the domain name is under the control of the curator of the collection, so they can demonstrate ownership of the collection. The later elements in the reverse DNS name can be used to disambiguate between multiple collections from the same curator. For example, `org.exampleos.Main` and `org.exampleos.Apps`. For the complete format of collection IDs, see [`ostree_validate_collection_id()`](reference__ostree-Core-repository-independent-functions.md#ostree-validate-collection-id "ostree_validate_collection_id ()").

## Functions

### ostree_repo_mode_from_string ()

``` programlisting
gboolean
ostree_repo_mode_from_string (const char *mode,
                              OstreeRepoMode *out_mode,
                              GError **error);
```

#### Parameters

|  |  |  |
|----|----|----|
| mode | a repo mode as a string |   |
| out_mode | the corresponding [OstreeRepoMode](reference__ostree-OstreeRepo.md#OstreeRepoMode "enum OstreeRepoMode"). | \[out\] |
| error | a GError if the string is not a valid mode |   |

------------------------------------------------------------------------

### ostree_repo_open_at ()

``` programlisting
OstreeRepo *
ostree_repo_open_at (int dfd,
                     const char *path,
                     GCancellable *cancellable,
                     GError **error);
```

This combines [`ostree_repo_new()`](reference__ostree-OstreeRepo.md#ostree-repo-new "ostree_repo_new ()") (but using fd-relative access) with [`ostree_repo_open()`](reference__ostree-OstreeRepo.md#ostree-repo-open "ostree_repo_open ()"). Use this when you know you should be operating on an already extant repository. If you want to create one, use [`ostree_repo_create_at()`](reference__ostree-OstreeRepo.md#ostree-repo-create-at "ostree_repo_create_at ()").

#### Parameters

|      |              |     |
|------|--------------|-----|
| dfd  | Directory fd |     |
| path | Path         |     |

#### Returns

An accessor object for an OSTree repository located at *`dfd`* + *`path`* .

\[transfer full\]

Since: 2017.10

------------------------------------------------------------------------

### ostree_repo_new ()

``` programlisting
OstreeRepo *
ostree_repo_new (GFile *path);
```

#### Parameters

|      |                      |     |
|------|----------------------|-----|
| path | Path to a repository |     |

#### Returns

An accessor object for an OSTree repository located at *`path`* .

\[transfer full\]

------------------------------------------------------------------------

### ostree_repo_new_for_sysroot_path ()

``` programlisting
OstreeRepo *
ostree_repo_new_for_sysroot_path (GFile *repo_path,
                                  GFile *sysroot_path);
```

Creates a new [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") instance, taking the system root path explicitly instead of assuming "/".

#### Parameters

|              |                         |     |
|--------------|-------------------------|-----|
| repo_path    | Path to a repository    |     |
| sysroot_path | Path to the system root |     |

#### Returns

An accessor object for the OSTree repository located at *`repo_path`* .

\[transfer full\]

------------------------------------------------------------------------

### ostree_repo_new_default ()

``` programlisting
OstreeRepo *
ostree_repo_new_default (void);
```

If the current working directory appears to be an OSTree repository, create a new [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") object for accessing it. Otherwise use the path in the OSTREE_REPO environment variable (if defined) or else the default system repository located at /ostree/repo.

#### Returns

An accessor object for an OSTree repository located at /ostree/repo.

\[transfer full\]

------------------------------------------------------------------------

### ostree_repo_open ()

``` programlisting
gboolean
ostree_repo_open (OstreeRepo *self,
                  GCancellable *cancellable,
                  GError **error);
```

------------------------------------------------------------------------

### ostree_repo_set_disable_fsync ()

``` programlisting
void
ostree_repo_set_disable_fsync (OstreeRepo *self,
                               gboolean disable_fsync);
```

Disable requests to `fsync()` to stable storage during commits. This option should only be used by build system tools which are creating disposable virtual machines, or have higher level mechanisms for ensuring data consistency.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| disable_fsync | If `TRUE`, do not fsync |   |

------------------------------------------------------------------------

### ostree_repo_get_disable_fsync ()

``` programlisting
gboolean
ostree_repo_get_disable_fsync (OstreeRepo *self);
```

For more information see [`ostree_repo_set_disable_fsync()`](reference__ostree-OstreeRepo.md#ostree-repo-set-disable-fsync "ostree_repo_set_disable_fsync ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |

#### Returns

Whether or not `fsync()` is enabled for this repo.

------------------------------------------------------------------------

### ostree_repo_is_system ()

``` programlisting
gboolean
ostree_repo_is_system (OstreeRepo *repo);
```

#### Parameters

|      |            |     |
|------|------------|-----|
| repo | Repository |     |

#### Returns

`TRUE` if this repository is the root-owned system global repository

------------------------------------------------------------------------

### ostree_repo_is_writable ()

``` programlisting
gboolean
ostree_repo_is_writable (OstreeRepo *self,
                         GError **error);
```

Returns whether the repository is writable by the current user. If the repository is not writable, the *`error`* indicates why.

#### Parameters

|       |          |     |
|-------|----------|-----|
| self  | Repo     |     |
| error | a GError |     |

#### Returns

`TRUE` if this repository is writable

------------------------------------------------------------------------

### ostree_repo_create_at ()

``` programlisting
OstreeRepo *
ostree_repo_create_at (int dfd,
                       const char *path,
                       OstreeRepoMode mode,
                       GVariant *options,
                       GCancellable *cancellable,
                       GError **error);
```

This is a file-descriptor relative version of [`ostree_repo_create()`](reference__ostree-OstreeRepo.md#ostree-repo-create "ostree_repo_create ()"). Create the underlying structure on disk for the repository, and call [`ostree_repo_open_at()`](reference__ostree-OstreeRepo.md#ostree-repo-open-at "ostree_repo_open_at ()") on the result, preparing it for use.

If a repository already exists at *`dfd`* + *`path`* (defined by an `objects/` subdirectory existing), then this function will simply call [`ostree_repo_open_at()`](reference__ostree-OstreeRepo.md#ostree-repo-open-at "ostree_repo_open_at ()"). In other words, this function cannot be used to change the mode or configuration (`repo/config`) of an existing repo.

The *`options`* dict may contain:

- collection-id: s: Set as collection ID in repo/config (Since 2017.9)

#### Parameters

|             |                                     |              |
|-------------|-------------------------------------|--------------|
| dfd         | Directory fd                        |              |
| path        | Path                                |              |
| mode        | The mode to store the repository in |              |
| options     | a{sv}: See below for accepted keys. | \[nullable\] |
| cancellable | Cancellable                         |              |
| error       | Error                               |              |

#### Returns

A new OSTree repository reference.

\[transfer full\]

Since: 2017.10

------------------------------------------------------------------------

### ostree_repo_create ()

``` programlisting
gboolean
ostree_repo_create (OstreeRepo *self,
                    OstreeRepoMode mode,
                    GCancellable *cancellable,
                    GError **error);
```

Create the underlying structure on disk for the repository, and call [`ostree_repo_open()`](reference__ostree-OstreeRepo.md#ostree-repo-open "ostree_repo_open ()") on the result, preparing it for use.

Since version 2016.8, this function will succeed on an existing repository, and finish creating any necessary files in a partially created repository. However, this function cannot change the mode of an existing repository, and will silently ignore an attempt to do so.

Since 2017.9, "existing repository" is defined by the existence of an `objects` subdirectory.

This function predates [`ostree_repo_create_at()`](reference__ostree-OstreeRepo.md#ostree-repo-create-at "ostree_repo_create_at ()"). It is an error to call this function on a repository initialized via [`ostree_repo_open_at()`](reference__ostree-OstreeRepo.md#ostree-repo-open-at "ostree_repo_open_at ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| mode | The mode to store the repository in |   |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_get_collection_id ()

``` programlisting
const gchar *
ostree_repo_get_collection_id (OstreeRepo *self);
```

Get the collection ID of this repository. See collection IDs.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |

#### Returns

collection ID for the repository.

\[nullable\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_get_bootloader ()

``` programlisting
const gchar *
ostree_repo_get_bootloader (OstreeRepo *self);
```

Get the bootloader configured. See the documentation for the "sysroot.bootloader" config key.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |

#### Returns

bootloader configuration for the sysroot.

\[transfer none\]

Since: 2019.2

------------------------------------------------------------------------

### ostree_repo_get_path ()

``` programlisting
GFile *
ostree_repo_get_path (OstreeRepo *self);
```

Note that since the introduction of [`ostree_repo_open_at()`](reference__ostree-OstreeRepo.md#ostree-repo-open-at "ostree_repo_open_at ()"), this function may return a process-specific path in `/proc` if the repository was created using that API. In general, you should avoid use of this API.

#### Parameters

|      |      |     |
|------|------|-----|
| self | Repo |     |

#### Returns

Path to repo.

\[transfer none\]

------------------------------------------------------------------------

### ostree_repo_get_mode ()

``` programlisting
OstreeRepoMode
ostree_repo_get_mode (OstreeRepo *self);
```

------------------------------------------------------------------------

### ostree_repo_get_min_free_space_bytes ()

``` programlisting
gboolean
ostree_repo_get_min_free_space_bytes (OstreeRepo *self,
                                      guint64 *out_reserved_bytes,
                                      GError **error);
```

Determine the number of bytes of free disk space that are reserved according to the repo config and return that number in *`out_reserved_bytes`* . See the documentation for the core.min-free-space-size and core.min-free-space-percent repo config options.

#### Parameters

|                    |                               |         |
|--------------------|-------------------------------|---------|
| self               | Repo                          |         |
| out_reserved_bytes | Location to store the result. | \[out\] |
| error              | Return location for a GError  |         |

#### Returns

`TRUE` on success, `FALSE` otherwise.

Since: 2018.9

------------------------------------------------------------------------

### ostree_repo_get_config ()

``` programlisting
GKeyFile *
ostree_repo_get_config (OstreeRepo *self);
```

#### Returns

The repository configuration; do not modify.

\[transfer none\]

------------------------------------------------------------------------

### ostree_repo_get_dfd ()

``` programlisting
int
ostree_repo_get_dfd (OstreeRepo *self);
```

In some cases it's useful for applications to access the repository directly; for example, writing content into `repo/tmp` ensures it's on the same filesystem. Another case is detecting the mtime on the repository (to see whether a ref was written).

#### Parameters

|      |      |     |
|------|------|-----|
| self | Repo |     |

#### Returns

File descriptor for repository root - owned by *`self`*

Since: 2016.4

------------------------------------------------------------------------

### ostree_repo_get_default_repo_finders ()

``` programlisting
const gchar *const *
ostree_repo_get_default_repo_finders (OstreeRepo *self);
```

Get the set of default repo finders configured. See the documentation for the "core.default-repo-finders" config key.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |

#### Returns

`NULL`-terminated array of strings.

\[array zero-terminated=1\]\[element-type utf8\]

Since: 2018.9

------------------------------------------------------------------------

### ostree_repo_lock_pop ()

``` programlisting
gboolean
ostree_repo_lock_pop (OstreeRepo *self,
                      OstreeRepoLockType lock_type,
                      GCancellable *cancellable,
                      GError **error);
```

Release a lock of type *`lock_type`* from the lock state. If the lock state becomes empty, the repository is unlocked. Otherwise, the lock state only changes when transitioning from an exclusive lock back to a shared lock. The requested *`lock_type`* must be the same type that was requested in the call to [`ostree_repo_lock_push()`](reference__ostree-OstreeRepo.md#ostree-repo-lock-push "ostree_repo_lock_push ()"). It is a programmer error if these do not match and the program may abort if the lock would reach an invalid state.

ostree_repo_lock_pop() waits for the lock depending on the repository's lock-timeout-secs configuration. When lock-timeout-secs is -1, a blocking lock is attempted. Otherwise, the lock is removed non-blocking and [`ostree_repo_lock_pop()`](reference__ostree-OstreeRepo.md#ostree-repo-lock-pop "ostree_repo_lock_pop ()") will sleep synchronously up to lock-timeout-secs seconds attempting to remove the lock. If the lock cannot be removed within the timeout, a `G_IO_ERROR_WOULD_BLOCK` error is returned.

If *`self`* is not writable by the user, then no unlocking is attempted and `TRUE` is returned.

#### Parameters

|  |  |  |
|----|----|----|
| self | a [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| lock_type | the type of lock to release |   |
| cancellable | a GCancellable |   |
| error | a GError |   |

#### Returns

`TRUE` on success, otherwise `FALSE` with *`error`* set

Since: 2021.3

------------------------------------------------------------------------

### ostree_repo_lock_push ()

``` programlisting
gboolean
ostree_repo_lock_push (OstreeRepo *self,
                       OstreeRepoLockType lock_type,
                       GCancellable *cancellable,
                       GError **error);
```

Takes a lock on the repository and adds it to the lock state. If *`lock_type`* is [`OSTREE_REPO_LOCK_SHARED`](reference__ostree-OstreeRepo.md#OSTREE-REPO-LOCK-SHARED:CAPS), a shared lock is taken. If *`lock_type`* is [`OSTREE_REPO_LOCK_EXCLUSIVE`](reference__ostree-OstreeRepo.md#OSTREE-REPO-LOCK-EXCLUSIVE:CAPS), an exclusive lock is taken. The actual lock state is only changed when locking a previously unlocked repository or upgrading the lock from shared to exclusive. If the requested lock type is unchanged or would represent a downgrade (exclusive to shared), the lock state is not changed.

ostree_repo_lock_push() waits for the lock depending on the repository's lock-timeout-secs configuration. When lock-timeout-secs is -1, a blocking lock is attempted. Otherwise, the lock is taken non-blocking and [`ostree_repo_lock_push()`](reference__ostree-OstreeRepo.md#ostree-repo-lock-push "ostree_repo_lock_push ()") will sleep synchronously up to lock-timeout-secs seconds attempting to acquire the lock. If the lock cannot be acquired within the timeout, a `G_IO_ERROR_WOULD_BLOCK` error is returned.

If *`self`* is not writable by the user, then no locking is attempted and `TRUE` is returned.

#### Parameters

|  |  |  |
|----|----|----|
| self | a [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| lock_type | the type of lock to acquire |   |
| cancellable | a GCancellable |   |
| error | a GError |   |

#### Returns

`TRUE` on success, otherwise `FALSE` with *`error`* set

Since: 2021.3

------------------------------------------------------------------------

### ostree_repo_auto_lock_push ()

``` programlisting
OstreeRepoAutoLock *
ostree_repo_auto_lock_push (OstreeRepo *self,
                            OstreeRepoLockType lock_type,
                            GCancellable *cancellable,
                            GError **error);
```

Like [`ostree_repo_lock_push()`](reference__ostree-OstreeRepo.md#ostree-repo-lock-push "ostree_repo_lock_push ()"), but for usage with [OstreeRepoAutoLock](reference__ostree-OstreeRepo.md#OstreeRepoAutoLock "OstreeRepoAutoLock"). The intended usage is to declare the [OstreeRepoAutoLock](reference__ostree-OstreeRepo.md#OstreeRepoAutoLock "OstreeRepoAutoLock") with `g_autoptr()` so that [`ostree_repo_auto_lock_cleanup()`](reference__ostree-OstreeRepo.md#ostree-repo-auto-lock-cleanup "ostree_repo_auto_lock_cleanup ()") is called when it goes out of scope. This will automatically release the lock if it was acquired successfully.

[TABLE]

\[skip\]

#### Parameters

|  |  |  |
|----|----|----|
| self | a [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| lock_type | the type of lock to acquire |   |
| cancellable | a GCancellable |   |
| error | a GError |   |

#### Returns

*`self`* on success, otherwise `NULL` with *`error`* set

Since: 2021.3

------------------------------------------------------------------------

### ostree_repo_auto_lock_cleanup ()

``` programlisting
void
ostree_repo_auto_lock_cleanup (OstreeRepoAutoLock *lock);
```

A cleanup handler for use with [`ostree_repo_auto_lock_push()`](reference__ostree-OstreeRepo.md#ostree-repo-auto-lock-push "ostree_repo_auto_lock_push ()"). If *`lock`* is not `NULL`, [`ostree_repo_lock_pop()`](reference__ostree-OstreeRepo.md#ostree-repo-lock-pop "ostree_repo_lock_pop ()") will be called on it. If [`ostree_repo_lock_pop()`](reference__ostree-OstreeRepo.md#ostree-repo-lock-pop "ostree_repo_lock_pop ()") fails, a critical warning will be emitted.

\[skip\]

#### Parameters

|  |  |  |
|----|----|----|
| lock | a [OstreeRepoAutoLock](reference__ostree-OstreeRepo.md#OstreeRepoAutoLock "OstreeRepoAutoLock") |   |

Since: 2021.3

------------------------------------------------------------------------

### ostree_repo_hash ()

``` programlisting
guint
ostree_repo_hash (OstreeRepo *self);
```

Calculate a hash value for the given open repository, suitable for use when putting it into a hash table. It is an error to call this on an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") which is not yet open, as a persistent hash value cannot be calculated until the repository is open and the inode of its root directory has been loaded.

This function does no I/O.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |

#### Returns

hash value for the [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo")

Since: 2017.12

------------------------------------------------------------------------

### ostree_repo_equal ()

``` programlisting
gboolean
ostree_repo_equal (OstreeRepo *a,
                   OstreeRepo *b);
```

Check whether two opened repositories are the same on disk: if their root directories are the same inode. If *`a`* or *`b`* are not open yet (due to [`ostree_repo_open()`](reference__ostree-OstreeRepo.md#ostree-repo-open "ostree_repo_open ()") not being called on them yet), `FALSE` will be returned.

#### Parameters

|  |  |  |
|----|----|----|
| a | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| b | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |

#### Returns

`TRUE` if *`a`* and *`b`* are the same repository on disk, `FALSE` otherwise

Since: 2017.12

------------------------------------------------------------------------

### ostree_repo_copy_config ()

``` programlisting
GKeyFile *
ostree_repo_copy_config (OstreeRepo *self);
```

#### Returns

A newly-allocated copy of the repository config.

\[transfer full\]

------------------------------------------------------------------------

### ostree_repo_remote_add ()

``` programlisting
gboolean
ostree_repo_remote_add (OstreeRepo *self,
                        const char *name,
                        const char *url,
                        GVariant *options,
                        GCancellable *cancellable,
                        GError **error);
```

Create a new remote named *`name`* pointing to *`url`* . If *`options`* is provided, then it will be mapped to GKeyFile entries, where the GVariant dictionary key is an option string, and the value is mapped as follows:

- s: `g_key_file_set_string()`

- b: `g_key_file_set_boolean()`

- as: `g_key_file_set_string_list()`

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| name | Name of remote |   |
| url | URL for remote (if URL begins with metalink=, it will be used as such). | \[allow-none\] |
| options | GVariant of type a{sv}. | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_remote_delete ()

``` programlisting
gboolean
ostree_repo_remote_delete (OstreeRepo *self,
                           const char *name,
                           GCancellable *cancellable,
                           GError **error);
```

Delete the remote named *`name`* . It is an error if the provided remote does not exist.

#### Parameters

|             |                |     |
|-------------|----------------|-----|
| self        | Repo           |     |
| name        | Name of remote |     |
| cancellable | Cancellable    |     |
| error       | Error          |     |

------------------------------------------------------------------------

### ostree_repo_remote_change ()

``` programlisting
gboolean
ostree_repo_remote_change (OstreeRepo *self,
                           GFile *sysroot,
                           OstreeRepoRemoteChange changeop,
                           const char *name,
                           const char *url,
                           GVariant *options,
                           GCancellable *cancellable,
                           GError **error);
```

A combined function handling the equivalent of [`ostree_repo_remote_add()`](reference__ostree-OstreeRepo.md#ostree-repo-remote-add "ostree_repo_remote_add ()"), [`ostree_repo_remote_delete()`](reference__ostree-OstreeRepo.md#ostree-repo-remote-delete "ostree_repo_remote_delete ()"), with more options.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| sysroot | System root. | \[allow-none\] |
| changeop | Operation to perform |   |
| name | Name of remote |   |
| url | URL for remote (if URL begins with metalink=, it will be used as such). | \[allow-none\] |
| options | GVariant of type a{sv}. | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_remote_list ()

``` programlisting
char **
ostree_repo_remote_list (OstreeRepo *self,
                         guint *out_n_remotes);
```

List available remote names in an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo"). Remote names are sorted alphabetically. If no remotes are available the function returns `NULL`.

#### Parameters

|               |                              |                       |
|---------------|------------------------------|-----------------------|
| self          | Repo                         |                       |
| out_n_remotes | Number of remotes available. | \[out\]\[allow-none\] |

#### Returns

a `NULL`-terminated array of remote names.

\[array length=out_n_remotes\]\[transfer full\]

------------------------------------------------------------------------

### ostree_repo_remote_list_collection_refs ()

``` programlisting
gboolean
ostree_repo_remote_list_collection_refs
                               (OstreeRepo *self,
                                const char *remote_name,
                                GHashTable **out_all_refs,
                                GCancellable *cancellable,
                                GError **error);
```

List refs advertised by *`remote_name`* , including refs which are part of collections. If the repository at *`remote_name`* has a collection ID set, its refs will be returned with that collection ID; otherwise, they will be returned with a `NULL` collection ID in each OstreeCollectionRef key in *`out_all_refs`* . Any refs for other collections stored in the repository will also be returned. No filtering is performed.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| remote_name | Name of the remote. |   |
| out_all_refs | Mapping from collection–ref to checksum. | \[out\]\[element-type OstreeCollectionRef utf8\]\[transfer container\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_remote_get_url ()

``` programlisting
gboolean
ostree_repo_remote_get_url (OstreeRepo *self,
                            const char *name,
                            char **out_url,
                            GError **error);
```

Return the URL of the remote named *`name`* through *`out_url`* . It is an error if the provided remote does not exist.

#### Parameters

|         |                |                     |
|---------|----------------|---------------------|
| self    | Repo           |                     |
| name    | Name of remote |                     |
| out_url | Remote's URL.  | \[out\]\[optional\] |
| error   | Error          |                     |

#### Returns

`TRUE` on success, `FALSE` on failure

------------------------------------------------------------------------

### ostree_repo_remote_get_gpg_verify ()

``` programlisting
gboolean
ostree_repo_remote_get_gpg_verify (OstreeRepo *self,
                                   const char *name,
                                   gboolean *out_gpg_verify,
                                   GError **error);
```

Return whether GPG verification is enabled for the remote named *`name`* through *`out_gpg_verify`* . It is an error if the provided remote does not exist.

#### Parameters

|                |                      |                     |
|----------------|----------------------|---------------------|
| self           | Repo                 |                     |
| name           | Name of remote       |                     |
| out_gpg_verify | Remote's GPG option. | \[out\]\[optional\] |
| error          | Error                |                     |

#### Returns

`TRUE` on success, `FALSE` on failure

------------------------------------------------------------------------

### ostree_repo_remote_get_gpg_verify_summary ()

``` programlisting
gboolean
ostree_repo_remote_get_gpg_verify_summary
                               (OstreeRepo *self,
                                const char *name,
                                gboolean *out_gpg_verify_summary,
                                GError **error);
```

Return whether GPG verification of the summary is enabled for the remote named *`name`* through *`out_gpg_verify_summary`* . It is an error if the provided remote does not exist.

#### Parameters

|                        |                      |                       |
|------------------------|----------------------|-----------------------|
| self                   | Repo                 |                       |
| name                   | Name of remote       |                       |
| out_gpg_verify_summary | Remote's GPG option. | \[out\]\[allow-none\] |
| error                  | Error                |                       |

#### Returns

`TRUE` on success, `FALSE` on failure

------------------------------------------------------------------------

### ostree_repo_remote_get_gpg_keys ()

``` programlisting
gboolean
ostree_repo_remote_get_gpg_keys (OstreeRepo *self,
                                 const char *name,
                                 const char *const *key_ids,
                                 GPtrArray **out_keys,
                                 GCancellable *cancellable,
                                 GError **error);
```

Enumerate the trusted GPG keys for the remote *`name`* . If *`name`* is `NULL`, the global GPG keys will be returned. The keys will be returned in the *`out_keys`* GPtrArray. Each element in the array is a GVariant of format `OSTREE_GPG_KEY_GVARIANT_FORMAT`. The *`key_ids`* array can be used to limit which keys are included. If *`key_ids`* is `NULL`, then all keys are included.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| name | name of the remote or `NULL`. | \[nullable\] |
| key_ids | a `NULL`-terminated array of GPG key IDs to include, or `NULL`. | \[array zero-terminated=1\]\[element-type utf8\]\[nullable\] |
| out_keys | return location for a GPtrArray of the remote's trusted GPG keys, or `NULL`. | \[out\]\[optional\]\[element-type GVariant\]\[transfer container\] |
| cancellable | a GCancellable, or `NULL`. | \[nullable\] |
| error | return location for a GError, or `NULL` |   |

#### Returns

`TRUE` if the GPG keys could be enumerated, `FALSE` otherwise

Since: 2021.4

------------------------------------------------------------------------

### ostree_repo_remote_gpg_import ()

``` programlisting
gboolean
ostree_repo_remote_gpg_import (OstreeRepo *self,
                               const char *name,
                               GInputStream *source_stream,
                               const char *const *key_ids,
                               guint *out_imported,
                               GCancellable *cancellable,
                               GError **error);
```

Imports one or more GPG keys from the open *`source_stream`* , or from the user's personal keyring if *`source_stream`* is `NULL`. The *`key_ids`* array can optionally restrict which keys are imported. If *`key_ids`* is `NULL`, then all keys are imported.

The imported keys will be used to conduct GPG verification when pulling from the remote named *`name`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Self |   |
| name | name of a remote |   |
| source_stream | a GInputStream, or `NULL`. | \[nullable\] |
| key_ids | a `NULL`-terminated array of GPG key IDs, or `NULL`. | \[array zero-terminated=1\]\[element-type utf8\]\[nullable\] |
| out_imported | return location for the number of imported keys, or `NULL`. | \[out\]\[optional\] |
| cancellable | a GCancellable |   |
| error | a GError |   |

#### Returns

`TRUE` on success, `FALSE` on failure

------------------------------------------------------------------------

### ostree_repo_remote_fetch_summary ()

``` programlisting
gboolean
ostree_repo_remote_fetch_summary (OstreeRepo *self,
                                  const char *name,
                                  GBytes **out_summary,
                                  GBytes **out_signatures,
                                  GCancellable *cancellable,
                                  GError **error);
```

Tries to fetch the summary file and any GPG signatures on the summary file over HTTP, and returns the binary data in *`out_summary`* and *`out_signatures`* respectively.

If no summary file exists on the remote server, *`out_summary`* is set to *`NULL`* . Likewise if the summary file is not signed, *`out_signatures`* is set to *`NULL`* . In either case the function still returns `TRUE`.

This method does not verify the signature of the downloaded summary file. Use [`ostree_repo_verify_summary()`](reference__ostree-OstreeRepo.md#ostree-repo-verify-summary "ostree_repo_verify_summary ()") for that.

Parse the summary data into a GVariant using `g_variant_new_from_bytes()` with [OSTREE_SUMMARY_GVARIANT_FORMAT](reference__ostree-Core-repository-independent-functions.md#OSTREE-SUMMARY-GVARIANT-FORMAT:CAPS "OSTREE_SUMMARY_GVARIANT_FORMAT") as the format string.

#### Parameters

|  |  |  |
|----|----|----|
| self | Self |   |
| name | name of a remote |   |
| out_summary | return location for raw summary data, or `NULL`. | \[out\]\[optional\] |
| out_signatures | return location for raw summary signature data, or `NULL`. | \[out\]\[optional\] |
| cancellable | a GCancellable |   |
| error | a GError |   |

#### Returns

`TRUE` on success, `FALSE` on failure

------------------------------------------------------------------------

### ostree_repo_remote_fetch_summary_with_options ()

``` programlisting
gboolean
ostree_repo_remote_fetch_summary_with_options
                               (OstreeRepo *self,
                                const char *name,
                                GVariant *options,
                                GBytes **out_summary,
                                GBytes **out_signatures,
                                GCancellable *cancellable,
                                GError **error);
```

Like [`ostree_repo_remote_fetch_summary()`](reference__ostree-OstreeRepo.md#ostree-repo-remote-fetch-summary "ostree_repo_remote_fetch_summary ()"), but supports an extensible set of flags. The following are currently defined:

- override-url (s): Fetch summary from this URL if remote specifies no metalink in options

- http-headers (a(ss)): Additional headers to add to all HTTP requests

- append-user-agent (s): Additional string to append to the user agent

- n-network-retries (u): Number of times to retry each download on receiving a transient network error, such as a socket timeout; default is 5, 0 means return errors without retrying

#### Parameters

|  |  |  |
|----|----|----|
| self | Self |   |
| name | name of a remote |   |
| options | A GVariant a{sv} with an extensible set of flags. | \[nullable\] |
| out_summary | return location for raw summary data, or `NULL`. | \[out\]\[optional\] |
| out_signatures | return location for raw summary signature data, or `NULL`. | \[out\]\[optional\] |
| cancellable | a GCancellable |   |
| error | a GError |   |

#### Returns

`TRUE` on success, `FALSE` on failure

Since: 2016.6

------------------------------------------------------------------------

### ostree_repo_reload_config ()

``` programlisting
gboolean
ostree_repo_reload_config (OstreeRepo *self,
                           GCancellable *cancellable,
                           GError **error);
```

By default, an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") will cache the remote configuration and its own repo/config data. This API can be used to reload it.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | repo        |     |
| cancellable | cancellable |     |
| error       | error       |     |

Since: 2017.2

------------------------------------------------------------------------

### ostree_repo_get_remote_boolean_option ()

``` programlisting
gboolean
ostree_repo_get_remote_boolean_option (OstreeRepo *self,
                                       const char *remote_name,
                                       const char *option_name,
                                       gboolean default_value,
                                       gboolean *out_value,
                                       GError **error);
```

OSTree remotes are represented by keyfile groups, formatted like: `[remote "remotename"]`. This function returns a value named *`option_name`* underneath that group, and returns it as a boolean. If the option is not set, *`out_value`* will be set to *`default_value`* . If an error is returned, *`out_value`* will be set to `FALSE`.

#### Parameters

|               |                                                  |     |
|---------------|--------------------------------------------------|-----|
| self          | A OstreeRepo                                     |     |
| remote_name   | Name                                             |     |
| option_name   | Option                                           |     |
| default_value | Value returned if *`option_name`* is not present |     |
| out_value     | (out) : location to store the result.            |     |
| error         | Error                                            |     |

#### Returns

`TRUE` on success, otherwise `FALSE` with *`error`* set

Since: 2016.5

------------------------------------------------------------------------

### ostree_repo_get_remote_list_option ()

``` programlisting
gboolean
ostree_repo_get_remote_list_option (OstreeRepo *self,
                                    const char *remote_name,
                                    const char *option_name,
                                    char ***out_value,
                                    GError **error);
```

OSTree remotes are represented by keyfile groups, formatted like: `[remote "remotename"]`. This function returns a value named *`option_name`* underneath that group, and returns it as a zero terminated array of strings. If the option is not set, or if an error is returned, *`out_value`* will be set to `NULL`.

#### Parameters

|  |  |  |
|----|----|----|
| self | A OstreeRepo |   |
| remote_name | Name |   |
| option_name | Option |   |
| out_value | location to store the list of strings. The list should be freed with `g_strfreev()`. | \[out\]\[array zero-terminated=1\] |
| error | Error |   |

#### Returns

`TRUE` on success, otherwise `FALSE` with *`error`* set

Since: 2016.5

------------------------------------------------------------------------

### ostree_repo_get_remote_option ()

``` programlisting
gboolean
ostree_repo_get_remote_option (OstreeRepo *self,
                               const char *remote_name,
                               const char *option_name,
                               const char *default_value,
                               char **out_value,
                               GError **error);
```

OSTree remotes are represented by keyfile groups, formatted like: `[remote "remotename"]`. This function returns a value named *`option_name`* underneath that group, or *`default_value`* if the remote exists but not the option name. If an error is returned, *`out_value`* will be set to `NULL`.

#### Parameters

|  |  |  |
|----|----|----|
| self | A OstreeRepo |   |
| remote_name | Name |   |
| option_name | Option |   |
| default_value | Value returned if *`option_name`* is not present. | \[nullable\] |
| out_value | Return location for value. | \[out\]\[nullable\] |
| error | Error |   |

#### Returns

`TRUE` on success, otherwise `FALSE` with *`error`* set

Since: 2016.5

------------------------------------------------------------------------

### ostree_repo_get_parent ()

``` programlisting
OstreeRepo *
ostree_repo_get_parent (OstreeRepo *self);
```

Before this function can be used, `ostree_repo_init()` must have been called.

#### Parameters

|      |      |     |
|------|------|-----|
| self | Repo |     |

#### Returns

Parent repository, or `NULL` if none.

\[transfer none\]\[nullable\]

------------------------------------------------------------------------

### ostree_repo_write_config ()

``` programlisting
gboolean
ostree_repo_write_config (OstreeRepo *self,
                          GKeyFile *new_config,
                          GError **error);
```

Save *`new_config`* in place of this repository's config file.

Note: This will not validate many elements of the configuration. Prefer `ostree_repo_write_config_and_reload`.

#### Parameters

|            |                                          |     |
|------------|------------------------------------------|-----|
| self       | Repo                                     |     |
| new_config | Overwrite the config file with this data |     |
| error      | a GError                                 |     |

------------------------------------------------------------------------

### ostree_repo_write_config_and_reload ()

``` programlisting
gboolean
ostree_repo_write_config_and_reload (OstreeRepo *self,
                                     GKeyFile *new_config,
                                     GError **error);
```

Save *`new_config`* in place of this repository's config file and reload. The config will be validated.

#### Parameters

|            |                                                      |     |
|------------|------------------------------------------------------|-----|
| self       | Repo                                                 |     |
| new_config | Overwrite the config file with this data, and reload |     |
| error      | a GError                                             |     |

------------------------------------------------------------------------

### ostree_repo_scan_hardlinks ()

``` programlisting
gboolean
ostree_repo_scan_hardlinks (OstreeRepo *self,
                            GCancellable *cancellable,
                            GError **error);
```

This function is deprecated in favor of using [`ostree_repo_devino_cache_new()`](reference__ostree-OstreeRepo.md#ostree-repo-devino-cache-new "ostree_repo_devino_cache_new ()"), which allows a precise mapping to be built up between hardlink checkout files and their checksums between [`ostree_repo_checkout_at()`](reference__ostree-OstreeRepo.md#ostree-repo-checkout-at "ostree_repo_checkout_at ()") and [`ostree_repo_write_directory_to_mtree()`](reference__ostree-OstreeRepo.md#ostree-repo-write-directory-to-mtree "ostree_repo_write_directory_to_mtree ()").

When invoking [`ostree_repo_write_directory_to_mtree()`](reference__ostree-OstreeRepo.md#ostree-repo-write-directory-to-mtree "ostree_repo_write_directory_to_mtree ()"), it has to compute the checksum of all files. If your commit contains hardlinks from a checkout, this functions builds a mapping of device numbers and inodes to their checksum.

There is an upfront cost to creating this mapping, as this will scan the entire objects directory. If your commit is composed of mostly hardlinks to existing ostree objects, then this will speed up considerably, so call it before you call [`ostree_repo_write_directory_to_mtree()`](reference__ostree-OstreeRepo.md#ostree-repo-write-directory-to-mtree "ostree_repo_write_directory_to_mtree ()") or similar. However, [`ostree_repo_devino_cache_new()`](reference__ostree-OstreeRepo.md#ostree-repo-devino-cache-new "ostree_repo_devino_cache_new ()") is better as it avoids scanning all objects.

Multithreading: This function is \*not\* MT safe.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_prepare_transaction ()

``` programlisting
gboolean
ostree_repo_prepare_transaction (OstreeRepo *self,
                                 gboolean *out_transaction_resume,
                                 GCancellable *cancellable,
                                 GError **error);
```

Starts or resumes a transaction. In order to write to a repo, you need to start a transaction. You can complete the transaction with [`ostree_repo_commit_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-transaction "ostree_repo_commit_transaction ()"), or abort the transaction with [`ostree_repo_abort_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-abort-transaction "ostree_repo_abort_transaction ()").

Currently, transactions may result in partial commits or data in the target repository if interrupted during [`ostree_repo_commit_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-transaction "ostree_repo_commit_transaction ()"), and further writing refs is also not currently atomic.

There can be at most one transaction active on a repo at a time per instance of `OstreeRepo`; however, it is safe to have multiple threads writing objects on a single `OstreeRepo` instance as long as their lifetime is bounded by the transaction.

Locking: Acquires a `shared` lock; release via commit or abort Multithreading: This function is \*not\* MT safe; only one transaction can be active at a time.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| out_transaction_resume | Whether this transaction is resuming from a previous one. This is a legacy state, now OSTree pulls use per-commit `state/.commitpartial` files. | \[allow-none\]\[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_commit_transaction ()

``` programlisting
gboolean
ostree_repo_commit_transaction (OstreeRepo *self,
                                OstreeRepoTransactionStats *out_stats,
                                GCancellable *cancellable,
                                GError **error);
```

Complete the transaction. Any refs set with [`ostree_repo_transaction_set_ref()`](reference__ostree-OstreeRepo.md#ostree-repo-transaction-set-ref "ostree_repo_transaction_set_ref ()") or [`ostree_repo_transaction_set_refspec()`](reference__ostree-OstreeRepo.md#ostree-repo-transaction-set-refspec "ostree_repo_transaction_set_refspec ()") will be written out.

Note that if multiple threads are performing writes, all such threads must have terminated before this function is invoked.

Locking: Releases `shared` lock acquired by [`ostree_repo_prepare_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-prepare-transaction "ostree_repo_prepare_transaction ()") Multithreading: This function is \*not\* MT safe; only one transaction can be active at a time.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| out_stats | A set of statistics of things that happened during this transaction. | \[allow-none\]\[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_abort_transaction ()

``` programlisting
gboolean
ostree_repo_abort_transaction (OstreeRepo *self,
                               GCancellable *cancellable,
                               GError **error);
```

Abort the active transaction; any staged objects and ref changes will be discarded. You \*must\* invoke this if you have chosen not to invoke [`ostree_repo_commit_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-transaction "ostree_repo_commit_transaction ()"). Calling this function when not in a transaction will do nothing and return successfully.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_transaction_set_refspec ()

``` programlisting
void
ostree_repo_transaction_set_refspec (OstreeRepo *self,
                                     const char *refspec,
                                     const char *checksum);
```

Like [`ostree_repo_transaction_set_ref()`](reference__ostree-OstreeRepo.md#ostree-repo-transaction-set-ref "ostree_repo_transaction_set_ref ()"), but takes concatenated *`refspec`* format as input instead of separate remote and name arguments.

Multithreading: Since v2017.15 this function is MT safe.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| refspec | The refspec to write |   |
| checksum | The checksum to point it to. | \[nullable\] |

------------------------------------------------------------------------

### ostree_repo_transaction_set_collection_ref ()

``` programlisting
void
ostree_repo_transaction_set_collection_ref
                               (OstreeRepo *self,
                                const OstreeCollectionRef *ref,
                                const char *checksum);
```

If *`checksum`* is not `NULL`, then record it as the target of local ref named *`ref`* .

Otherwise, if *`checksum`* is `NULL`, then record that the ref should be deleted.

The change will not be written out immediately, but when the transaction is completed with [`ostree_repo_commit_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-transaction "ostree_repo_commit_transaction ()"). If the transaction is instead aborted with [`ostree_repo_abort_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-abort-transaction "ostree_repo_abort_transaction ()"), no changes will be made to the repository.

Multithreading: Since v2017.15 this function is MT safe.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| ref | The collection–ref to write |   |
| checksum | The checksum to point it to. | \[nullable\] |

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_transaction_set_ref ()

``` programlisting
void
ostree_repo_transaction_set_ref (OstreeRepo *self,
                                 const char *remote,
                                 const char *ref,
                                 const char *checksum);
```

If *`checksum`* is not `NULL`, then record it as the target of ref named *`ref`* ; if *`remote`* is provided, the ref will appear to originate from that remote.

Otherwise, if *`checksum`* is `NULL`, then record that the ref should be deleted.

The change will be written when the transaction is completed with [`ostree_repo_commit_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-transaction "ostree_repo_commit_transaction ()"); that function takes care of writing all of the objects (such as the commit referred to by *`checksum`* ) before updating the refs. If the transaction is instead aborted with [`ostree_repo_abort_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-abort-transaction "ostree_repo_abort_transaction ()"), no changes to the ref will be made to the repository.

Note however that currently writing \*multiple\* refs is not truly atomic; if the process or system is terminated during [`ostree_repo_commit_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-transaction "ostree_repo_commit_transaction ()"), it is possible that just some of the refs will have been updated. Your application should take care to handle this case.

Multithreading: Since v2017.15 this function is MT safe.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| remote | A remote for the ref. | \[allow-none\] |
| ref | The ref to write |   |
| checksum | The checksum to point it to. | \[nullable\] |

------------------------------------------------------------------------

### ostree_repo_set_ref_immediate ()

``` programlisting
gboolean
ostree_repo_set_ref_immediate (OstreeRepo *self,
                               const char *remote,
                               const char *ref,
                               const char *checksum,
                               GCancellable *cancellable,
                               GError **error);
```

This is like [`ostree_repo_transaction_set_ref()`](reference__ostree-OstreeRepo.md#ostree-repo-transaction-set-ref "ostree_repo_transaction_set_ref ()"), except it may be invoked outside of a transaction. This is presently safe for the case where we're creating or overwriting an existing ref.

Multithreading: This function is MT safe.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| remote | A remote for the ref. | \[allow-none\] |
| ref | The ref to write |   |
| checksum | The checksum to point it to, or `NULL` to unset. | \[allow-none\] |
| cancellable | GCancellable |   |
| error | GError |   |

------------------------------------------------------------------------

### ostree_repo_set_alias_ref_immediate ()

``` programlisting
gboolean
ostree_repo_set_alias_ref_immediate (OstreeRepo *self,
                                     const char *remote,
                                     const char *ref,
                                     const char *target,
                                     GCancellable *cancellable,
                                     GError **error);
```

Like [`ostree_repo_set_ref_immediate()`](reference__ostree-OstreeRepo.md#ostree-repo-set-ref-immediate "ostree_repo_set_ref_immediate ()"), but creates an alias.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| remote | A remote for the ref. | \[allow-none\] |
| ref | The ref to write |   |
| target | The ref target to point it to, or `NULL` to unset. | \[allow-none\] |
| cancellable | GCancellable |   |
| error | GError |   |

Since: 2017.10

------------------------------------------------------------------------

### ostree_repo_set_cache_dir ()

``` programlisting
gboolean
ostree_repo_set_cache_dir (OstreeRepo *self,
                           int dfd,
                           const char *path,
                           GCancellable *cancellable,
                           GError **error);
```

Set a custom location for the cache directory used for e.g. per-remote summary caches. Setting this manually is useful when doing operations on a system repo as a user because you don't have write permissions in the repo, where the cache is normally stored.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| dfd | directory fd |   |
| path | subpath in *`dfd`* |   |
| cancellable | a GCancellable |   |
| error | a GError |   |

Since: 2016.5

------------------------------------------------------------------------

### ostree_repo_set_collection_id ()

``` programlisting
gboolean
ostree_repo_set_collection_id (OstreeRepo *self,
                               const gchar *collection_id,
                               GError **error);
```

Set or clear the collection ID of this repository. See collection IDs. The update will be made in memory, but must be written out to the repository configuration on disk using [`ostree_repo_write_config()`](reference__ostree-OstreeRepo.md#ostree-repo-write-config "ostree_repo_write_config ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| collection_id | new collection ID, or `NULL` to unset it. | \[nullable\] |
| error | return location for a GError, or `NULL` |   |

#### Returns

`TRUE` on success, `FALSE` otherwise

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_set_collection_ref_immediate ()

``` programlisting
gboolean
ostree_repo_set_collection_ref_immediate
                               (OstreeRepo *self,
                                const OstreeCollectionRef *ref,
                                const char *checksum,
                                GCancellable *cancellable,
                                GError **error);
```

This is like [`ostree_repo_transaction_set_collection_ref()`](reference__ostree-OstreeRepo.md#ostree-repo-transaction-set-collection-ref "ostree_repo_transaction_set_collection_ref ()"), except it may be invoked outside of a transaction. This is presently safe for the case where we're creating or overwriting an existing ref.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| ref | The collection–ref to write |   |
| checksum | The checksum to point it to, or `NULL` to unset. | \[nullable\] |
| cancellable | GCancellable |   |
| error | GError |   |

#### Returns

`TRUE` on success, `FALSE` otherwise

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_sign_delta ()

``` programlisting
gboolean
ostree_repo_sign_delta (OstreeRepo *self,
                        const gchar *from_commit,
                        const gchar *to_commit,
                        const gchar *key_id,
                        const gchar *homedir,
                        GCancellable *cancellable,
                        GError **error);
```

This function is deprecated, sign the summary file instead. Add a GPG signature to a static delta.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Self        |     |
| from_commit | From commit |     |
| to_commit   | To commit   |     |
| key_id      | key id      |     |
| homedir     | homedir     |     |
| cancellable | cancellable |     |
| error       | error       |     |

------------------------------------------------------------------------

### ostree_repo_has_object ()

``` programlisting
gboolean
ostree_repo_has_object (OstreeRepo *self,
                        OstreeObjectType objtype,
                        const char *checksum,
                        gboolean *out_have_object,
                        GCancellable *cancellable,
                        GError **error);
```

Set *`out_have_object`* to `TRUE` if *`self`* contains the given object; `FALSE` otherwise.

#### Parameters

|                 |                                       |         |
|-----------------|---------------------------------------|---------|
| self            | Repo                                  |         |
| objtype         | Object type                           |         |
| checksum        | ASCII SHA256 checksum                 |         |
| out_have_object | `TRUE` if repository contains object. | \[out\] |
| cancellable     | Cancellable                           |         |
| error           | Error                                 |         |

#### Returns

`FALSE` if an unexpected error occurred, `TRUE` otherwise

------------------------------------------------------------------------

### ostree_repo_mark_commit_partial ()

``` programlisting
gboolean
ostree_repo_mark_commit_partial (OstreeRepo *self,
                                 const char *checksum,
                                 gboolean is_partial,
                                 GError **error);
```

Commits in the "partial" state do not have all their child objects written. This occurs in various situations, such as during a pull, but also if a "subpath" pull is used, as well as "commit only" pulls.

This function is used by [`ostree_repo_pull_with_options()`](reference__ostree-OstreeRepo.md#ostree-repo-pull-with-options "ostree_repo_pull_with_options ()"); you should use this if you are implementing a different type of transport.

#### Parameters

|            |                                       |     |
|------------|---------------------------------------|-----|
| self       | Repo                                  |     |
| checksum   | Commit SHA-256                        |     |
| is_partial | Whether or not this commit is partial |     |
| error      | Error                                 |     |

Since: 2017.15

------------------------------------------------------------------------

### ostree_repo_mark_commit_partial_reason ()

``` programlisting
gboolean
ostree_repo_mark_commit_partial_reason
                               (OstreeRepo *self,
                                const char *checksum,
                                gboolean is_partial,
                                OstreeRepoCommitState in_state,
                                GError **error);
```

Allows the setting of a reason code for a partial commit. Presently it only supports setting reason bitmask to OSTREE_REPO_COMMIT_STATE_FSCK_PARTIAL, or OSTREE_REPO_COMMIT_STATE_NORMAL. This will allow successive ostree fsck operations to exit properly with an error code if the repository has been truncated as a result of fsck trying to repair it.

#### Parameters

|            |                                       |     |
|------------|---------------------------------------|-----|
| self       | Repo                                  |     |
| checksum   | Commit SHA-256                        |     |
| is_partial | Whether or not this commit is partial |     |
| in_state   | Reason bitmask for partial commit     |     |
| error      | Error                                 |     |

Since: 2019.4

------------------------------------------------------------------------

### ostree_repo_write_metadata ()

``` programlisting
gboolean
ostree_repo_write_metadata (OstreeRepo *self,
                            OstreeObjectType objtype,
                            const char *expected_checksum,
                            GVariant *object,
                            guchar **out_csum,
                            GCancellable *cancellable,
                            GError **error);
```

Store the metadata object *`object`* . Return the checksum as *`out_csum`* .

If *`expected_checksum`* is not `NULL`, verify it against the computed checksum.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| objtype | Object type |   |
| expected_checksum | If provided, validate content against this checksum. | \[nullable\] |
| object | Metadata |   |
| out_csum | Binary checksum. | \[out\]\[array fixed-size=32\]\[optional\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_write_metadata_async ()

``` programlisting
void
ostree_repo_write_metadata_async (OstreeRepo *self,
                                  OstreeObjectType objtype,
                                  const char *expected_checksum,
                                  GVariant *object,
                                  GCancellable *cancellable,
                                  GAsyncReadyCallback callback,
                                  gpointer user_data);
```

Asynchronously store the metadata object *`variant`* . If provided, the checksum *`expected_checksum`* will be verified.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| objtype | Object type |   |
| expected_checksum | If provided, validate content against this checksum. | \[nullable\] |
| object | Metadata |   |
| cancellable | Cancellable |   |
| callback | Invoked when metadata is writed |   |
| user_data | Data for *`callback`* |   |

------------------------------------------------------------------------

### ostree_repo_write_metadata_finish ()

``` programlisting
gboolean
ostree_repo_write_metadata_finish (OstreeRepo *self,
                                   GAsyncResult *result,
                                   guchar **out_csum,
                                   GError **error);
```

Complete a call to [`ostree_repo_write_metadata_async()`](reference__ostree-OstreeRepo.md#ostree-repo-write-metadata-async "ostree_repo_write_metadata_async ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| result | Result |   |
| out_csum | Binary checksum value. | \[out\]\[array fixed-size=32\]\[element-type guint8\] |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_write_content ()

``` programlisting
gboolean
ostree_repo_write_content (OstreeRepo *self,
                           const char *expected_checksum,
                           GInputStream *object_input,
                           guint64 length,
                           guchar **out_csum,
                           GCancellable *cancellable,
                           GError **error);
```

Store the content object streamed as *`object_input`* , with total length *`length`* . The actual checksum will be returned as *`out_csum`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| expected_checksum | If provided, validate content against this checksum. | \[allow-none\] |
| object_input | Content object stream |   |
| length | Length of *`object_input`* |   |
| out_csum | Binary checksum. | \[out\]\[array fixed-size=32\]\[optional\]\[nullable\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_write_regfile ()

``` programlisting
OstreeContentWriter *
ostree_repo_write_regfile (OstreeRepo *self,
                           const char *expected_checksum,
                           guint32 uid,
                           guint32 gid,
                           guint32 mode,
                           guint64 content_len,
                           GVariant *xattrs,
                           GError **error);
```

Create an `OstreeContentWriter` that allows streaming output into the repository.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo, |   |
| expected_checksum | Expected checksum (SHA-256 hex string). | \[allow-none\] |
| uid | user id |   |
| gid | group id |   |
| mode | Unix file mode |   |
| content_len | Expected content length |   |
| xattrs | Extended attributes (GVariant type `(ayay)`). | \[allow-none\] |
| error | Error |   |

#### Returns

A new writer, or `NULL` on error.

\[transfer full\]

Since: 2021.2

------------------------------------------------------------------------

### ostree_repo_write_regfile_inline ()

``` programlisting
char *
ostree_repo_write_regfile_inline (OstreeRepo *self,
                                  const char *expected_checksum,
                                  guint32 uid,
                                  guint32 gid,
                                  guint32 mode,
                                  GVariant *xattrs,
                                  const guint8 *buf,
                                  gsize len,
                                  GCancellable *cancellable,
                                  GError **error);
```

Synchronously create a file object from the provided content. This API is intended for small files where it is reasonable to buffer the entire content in memory.

Unlike [`ostree_repo_write_content()`](reference__ostree-OstreeRepo.md#ostree-repo-write-content "ostree_repo_write_content ()"), if *`expected_checksum`* is provided, this function will not check for the presence of the object beforehand.

#### Parameters

|  |  |  |
|----|----|----|
| self | repo |   |
| expected_checksum | The expected checksum. | \[allow-none\] |
| uid | User id |   |
| gid | Group id |   |
| mode | File mode |   |
| xattrs | Extended attributes, GVariant of type (ayay). | \[allow-none\] |
| buf | File contents. | \[array length=len\]\[element-type guint8\] |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

Checksum (as a hex string) of the committed file.

\[transfer full\]

Since: 2021.2

------------------------------------------------------------------------

### ostree_repo_write_symlink ()

``` programlisting
char *
ostree_repo_write_symlink (OstreeRepo *self,
                           const char *expected_checksum,
                           guint32 uid,
                           guint32 gid,
                           GVariant *xattrs,
                           const char *symlink_target,
                           GCancellable *cancellable,
                           GError **error);
```

Synchronously create a symlink object.

Unlike [`ostree_repo_write_content()`](reference__ostree-OstreeRepo.md#ostree-repo-write-content "ostree_repo_write_content ()"), if *`expected_checksum`* is provided, this function will not check for the presence of the object beforehand.

#### Parameters

|  |  |  |
|----|----|----|
| self | repo |   |
| expected_checksum | The expected checksum. | \[allow-none\] |
| uid | User id |   |
| gid | Group id |   |
| xattrs | Extended attributes, GVariant of type (ayay). | \[allow-none\] |
| symlink_target | Target of the symbolic link |   |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

Checksum (as a hex string) of the committed file.

\[transfer full\]

Since: 2021.2

------------------------------------------------------------------------

### ostree_repo_write_metadata_trusted ()

``` programlisting
gboolean
ostree_repo_write_metadata_trusted (OstreeRepo *self,
                                    OstreeObjectType objtype,
                                    const char *checksum,
                                    GVariant *variant,
                                    GCancellable *cancellable,
                                    GError **error);
```

Store the metadata object *`variant`* ; the provided *`checksum`* is trusted.

#### Parameters

|             |                                              |     |
|-------------|----------------------------------------------|-----|
| self        | Repo                                         |     |
| objtype     | Object type                                  |     |
| checksum    | Store object with this ASCII SHA256 checksum |     |
| variant     | Metadata object                              |     |
| cancellable | Cancellable                                  |     |
| error       | Error                                        |     |

------------------------------------------------------------------------

### ostree_repo_write_metadata_stream_trusted ()

``` programlisting
gboolean
ostree_repo_write_metadata_stream_trusted
                               (OstreeRepo *self,
                                OstreeObjectType objtype,
                                const char *checksum,
                                GInputStream *object_input,
                                guint64 length,
                                GCancellable *cancellable,
                                GError **error);
```

Store the metadata object *`variant`* ; the provided *`checksum`* is trusted.

#### Parameters

|              |                                              |     |
|--------------|----------------------------------------------|-----|
| self         | Repo                                         |     |
| objtype      | Object type                                  |     |
| checksum     | Store object with this ASCII SHA256 checksum |     |
| object_input | Metadata object stream                       |     |
| length       | Length, may be 0 for unknown                 |     |
| cancellable  | Cancellable                                  |     |
| error        | Error                                        |     |

------------------------------------------------------------------------

### ostree_repo_write_content_trusted ()

``` programlisting
gboolean
ostree_repo_write_content_trusted (OstreeRepo *self,
                                   const char *checksum,
                                   GInputStream *object_input,
                                   guint64 length,
                                   GCancellable *cancellable,
                                   GError **error);
```

Store the content object streamed as *`object_input`* , with total length *`length`* . The given *`checksum`* will be treated as trusted.

This function should be used when importing file objects from local disk, for example.

#### Parameters

|              |                                                |     |
|--------------|------------------------------------------------|-----|
| self         | Repo                                           |     |
| checksum     | Store content using this ASCII SHA256 checksum |     |
| object_input | Content stream                                 |     |
| length       | Length of *`object_input`*                     |     |
| cancellable  | Cancellable                                    |     |
| error        | Data for *`callback`*                          |     |

------------------------------------------------------------------------

### ostree_repo_write_content_async ()

``` programlisting
void
ostree_repo_write_content_async (OstreeRepo *self,
                                 const char *expected_checksum,
                                 GInputStream *object,
                                 guint64 length,
                                 GCancellable *cancellable,
                                 GAsyncReadyCallback callback,
                                 gpointer user_data);
```

Asynchronously store the content object *`object`* . If provided, the checksum *`expected_checksum`* will be verified.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| expected_checksum | If provided, validate content against this checksum. | \[allow-none\] |
| object | Input |   |
| length | Length of *`object`* |   |
| cancellable | Cancellable |   |
| callback | Invoked when content is writed |   |
| user_data | User data for *`callback`* |   |

------------------------------------------------------------------------

### ostree_repo_write_content_finish ()

``` programlisting
gboolean
ostree_repo_write_content_finish (OstreeRepo *self,
                                  GAsyncResult *result,
                                  guchar **out_csum,
                                  GError **error);
```

Completes an invocation of [`ostree_repo_write_content_async()`](reference__ostree-OstreeRepo.md#ostree-repo-write-content-async "ostree_repo_write_content_async ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | a [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| result | a GAsyncResult |   |
| out_csum | A binary SHA256 checksum of the content object. | \[out\]\[transfer full\]\[optional\] |
| error | a GError |   |

------------------------------------------------------------------------

### ostree_repo_resolve_rev ()

``` programlisting
gboolean
ostree_repo_resolve_rev (OstreeRepo *self,
                         const char *refspec,
                         gboolean allow_noent,
                         char **out_rev,
                         GError **error);
```

Look up the given refspec, returning the checksum it references in the parameter *`out_rev`* . Will fall back on remote directory if cannot find the given refspec in local.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| refspec | A refspec |   |
| allow_noent | Do not throw an error if refspec does not exist |   |
| out_rev | A checksum,or `NULL` if *`allow_noent`* is true and it does not exist. | \[out\]\[nullable\]\[transfer full\] |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_resolve_rev_ext ()

``` programlisting
gboolean
ostree_repo_resolve_rev_ext (OstreeRepo *self,
                             const char *refspec,
                             gboolean allow_noent,
                             OstreeRepoResolveRevExtFlags flags,
                             char **out_rev,
                             GError **error);
```

Look up the given refspec, returning the checksum it references in the parameter *`out_rev`* . Differently from [`ostree_repo_resolve_rev()`](reference__ostree-OstreeRepo.md#ostree-repo-resolve-rev "ostree_repo_resolve_rev ()"), this will not fall back to searching through remote repos if a local ref is specified but not found.

The flag [`OSTREE_REPO_RESOLVE_REV_EXT_LOCAL_ONLY`](reference__ostree-OstreeRepo.md#OSTREE-REPO-RESOLVE-REV-EXT-LOCAL-ONLY:CAPS) is implied so using it has no effect.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| refspec | A refspec |   |
| allow_noent | Do not throw an error if refspec does not exist |   |
| flags | Options controlling behavior |   |
| out_rev | A checksum,or `NULL` if *`allow_noent`* is true and it does not exist. | \[out\]\[nullable\]\[transfer full\] |
| error | Error |   |

Since: 2016.7

------------------------------------------------------------------------

### ostree_repo_list_refs ()

``` programlisting
gboolean
ostree_repo_list_refs (OstreeRepo *self,
                       const char *refspec_prefix,
                       GHashTable **out_all_refs,
                       GCancellable *cancellable,
                       GError **error);
```

If *`refspec_prefix`* is `NULL`, list all local and remote refspecs, with their current values in *`out_all_refs`* . Otherwise, only list refspecs which have *`refspec_prefix`* as a prefix.

*`out_all_refs`* will be returned as a mapping from refspecs (including the remote name) to checksums. If *`refspec_prefix`* is non-`NULL`, it will be removed as a prefix from the hash table keys.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| refspec_prefix | Only list refs which match this prefix. | \[allow-none\] |
| out_all_refs | Mapping from refspec to checksum. | \[out\]\[element-type utf8 utf8\]\[transfer container\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_list_refs_ext ()

``` programlisting
gboolean
ostree_repo_list_refs_ext (OstreeRepo *self,
                           const char *refspec_prefix,
                           GHashTable **out_all_refs,
                           OstreeRepoListRefsExtFlags flags,
                           GCancellable *cancellable,
                           GError **error);
```

If *`refspec_prefix`* is `NULL`, list all local and remote refspecs, with their current values in *`out_all_refs`* . Otherwise, only list refspecs which have *`refspec_prefix`* as a prefix.

*`out_all_refs`* will be returned as a mapping from refspecs (including the remote name) to checksums. Differently from [`ostree_repo_list_refs()`](reference__ostree-OstreeRepo.md#ostree-repo-list-refs "ostree_repo_list_refs ()"), the *`refspec_prefix`* will not be removed from the refspecs in the hash table.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| refspec_prefix | Only list refs which match this prefix. | \[allow-none\] |
| out_all_refs | Mapping from refspec to checksum. | \[out\]\[element-type utf8 utf8\]\[transfer container\] |
| flags | Options controlling listing behavior |   |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2016.4

------------------------------------------------------------------------

### ostree_repo_list_collection_refs ()

``` programlisting
gboolean
ostree_repo_list_collection_refs (OstreeRepo *self,
                                  const char *match_collection_id,
                                  GHashTable **out_all_refs,
                                  OstreeRepoListRefsExtFlags flags,
                                  GCancellable *cancellable,
                                  GError **error);
```

List all local, mirrored, and remote refs, mapping them to the commit checksums they currently point to in *`out_all_refs`* . If *`match_collection_id`* is specified, the results will be limited to those with an equal collection ID.

OstreeCollectionRefs are guaranteed to be returned with their collection ID set to a non-`NULL` value; so no refs from `refs/heads` will be listed if no collection ID is configured for the repository ([`ostree_repo_get_collection_id()`](reference__ostree-OstreeRepo.md#ostree-repo-get-collection-id "ostree_repo_get_collection_id ()")).

If you want to exclude refs from `refs/remotes`, use [`OSTREE_REPO_LIST_REFS_EXT_EXCLUDE_REMOTES`](reference__ostree-OstreeRepo.md#OSTREE-REPO-LIST-REFS-EXT-EXCLUDE-REMOTES:CAPS) in *`flags`* . Similarly use [`OSTREE_REPO_LIST_REFS_EXT_EXCLUDE_MIRRORS`](reference__ostree-OstreeRepo.md#OSTREE-REPO-LIST-REFS-EXT-EXCLUDE-MIRRORS:CAPS) to exclude refs from `refs/mirrors`.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| match_collection_id | If non-`NULL`, only list refs from this collection. | \[nullable\] |
| out_all_refs | Mapping from collection–ref to checksum. | \[out\]\[element-type OstreeCollectionRef utf8\]\[transfer container\] |
| flags | Options controlling listing behavior |   |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

`TRUE` on success, `FALSE` otherwise

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_remote_list_refs ()

``` programlisting
gboolean
ostree_repo_remote_list_refs (OstreeRepo *self,
                              const char *remote_name,
                              GHashTable **out_all_refs,
                              GCancellable *cancellable,
                              GError **error);
```

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| remote_name | Name of the remote. |   |
| out_all_refs | Mapping from ref to checksum. | \[out\]\[element-type utf8 utf8\]\[transfer container\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_resolve_collection_ref ()

``` programlisting
gboolean
ostree_repo_resolve_collection_ref (OstreeRepo *self,
                                    const OstreeCollectionRef *ref,
                                    gboolean allow_noent,
                                    OstreeRepoResolveRevExtFlags flags,
                                    char **out_rev,
                                    GCancellable *cancellable,
                                    GError **error);
```

Look up the checksum for the given collection–ref, returning it in *`out_rev`* . This will search through the mirrors and remote refs.

If *`allow_noent`* is `TRUE` and the given *`ref`* cannot be found, `TRUE` will be returned and *`out_rev`* will be set to `NULL`. If *`allow_noent`* is `FALSE` and the given *`ref`* cannot be found, a `G_IO_ERROR_NOT_FOUND` error will be returned.

If you want to check only local refs, not remote or mirrored ones, use the flag [`OSTREE_REPO_RESOLVE_REV_EXT_LOCAL_ONLY`](reference__ostree-OstreeRepo.md#OSTREE-REPO-RESOLVE-REV-EXT-LOCAL-ONLY:CAPS). This is analogous to using [`ostree_repo_resolve_rev_ext()`](reference__ostree-OstreeRepo.md#ostree-repo-resolve-rev-ext "ostree_repo_resolve_rev_ext ()") but for collection-refs.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| ref | a collection–ref to resolve |   |
| allow_noent | `TRUE` to not throw an error if *`ref`* doesn’t exist |   |
| flags | options controlling behaviour |   |
| out_rev | return location for the checksum corresponding to *`ref`* , or `NULL` if *`allow_noent`* is `TRUE` and the *`ref`* could not be found. | \[out\]\[transfer full\]\[optional\]\[nullable\] |
| cancellable | a GCancellable, or `NULL`. | \[nullable\] |
| error | return location for a GError, or `NULL` |   |

#### Returns

`TRUE` on success, `FALSE` on failure

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_load_variant ()

``` programlisting
gboolean
ostree_repo_load_variant (OstreeRepo *self,
                          OstreeObjectType objtype,
                          const char *sha256,
                          GVariant **out_variant,
                          GError **error);
```

Load the metadata object *`sha256`* of type *`objtype`* , storing the result in *`out_variant`* .

#### Parameters

|             |                      |                          |
|-------------|----------------------|--------------------------|
| self        | Repo                 |                          |
| objtype     | Expected object type |                          |
| sha256      | Checksum string      |                          |
| out_variant | Metadata object.     | \[out\]\[transfer full\] |
| error       | Error                |                          |

------------------------------------------------------------------------

### ostree_repo_load_commit ()

``` programlisting
gboolean
ostree_repo_load_commit (OstreeRepo *self,
                         const char *checksum,
                         GVariant **out_commit,
                         OstreeRepoCommitState *out_state,
                         GError **error);
```

A version of [`ostree_repo_load_variant()`](reference__ostree-OstreeRepo.md#ostree-repo-load-variant "ostree_repo_load_variant ()") specialized to commits, capable of returning extended state information. Currently the only extended state is [`OSTREE_REPO_COMMIT_STATE_PARTIAL`](reference__ostree-OstreeRepo.md#OSTREE-REPO-COMMIT-STATE-PARTIAL:CAPS), which means that only a sub-path of the commit is available.

#### Parameters

|            |                 |                       |
|------------|-----------------|-----------------------|
| self       | Repo            |                       |
| checksum   | Commit checksum |                       |
| out_commit | Commit.         | \[out\]\[allow-none\] |
| out_state  | Commit state.   | \[out\]\[allow-none\] |
| error      | Error           |                       |

------------------------------------------------------------------------

### ostree_repo_load_variant_if_exists ()

``` programlisting
gboolean
ostree_repo_load_variant_if_exists (OstreeRepo *self,
                                    OstreeObjectType objtype,
                                    const char *sha256,
                                    GVariant **out_variant,
                                    GError **error);
```

Attempt to load the metadata object *`sha256`* of type *`objtype`* if it exists, storing the result in *`out_variant`* . If it doesn't exist, *`out_variant`* will be set to `NULL` and the function will still return TRUE.

#### Parameters

|             |                |                                      |
|-------------|----------------|--------------------------------------|
| self        | Repo           |                                      |
| objtype     | Object type    |                                      |
| sha256      | ASCII checksum |                                      |
| out_variant | Metadata.      | \[out\]\[nullable\]\[transfer full\] |
| error       | Error          |                                      |

------------------------------------------------------------------------

### ostree_repo_load_file ()

``` programlisting
gboolean
ostree_repo_load_file (OstreeRepo *self,
                       const char *checksum,
                       GInputStream **out_input,
                       GFileInfo **out_file_info,
                       GVariant **out_xattrs,
                       GCancellable *cancellable,
                       GError **error);
```

Load content object, decomposing it into three parts: the actual content (for regular files), the metadata, and extended attributes.

#### Parameters

|               |                       |                                 |
|---------------|-----------------------|---------------------------------|
| self          | Repo                  |                                 |
| checksum      | ASCII SHA256 checksum |                                 |
| out_input     | File content.         | \[out\]\[optional\]\[nullable\] |
| out_file_info | File information.     | \[out\]\[optional\]\[nullable\] |
| out_xattrs    | Extended attributes.  | \[out\]\[optional\]\[nullable\] |
| cancellable   | Cancellable           |                                 |
| error         | Error                 |                                 |

------------------------------------------------------------------------

### ostree_repo_load_object_stream ()

``` programlisting
gboolean
ostree_repo_load_object_stream (OstreeRepo *self,
                                OstreeObjectType objtype,
                                const char *checksum,
                                GInputStream **out_input,
                                guint64 *out_size,
                                GCancellable *cancellable,
                                GError **error);
```

Load object as a stream; useful when copying objects between repositories.

#### Parameters

|             |                           |         |
|-------------|---------------------------|---------|
| self        | Repo                      |         |
| objtype     | Object type               |         |
| checksum    | ASCII SHA256 checksum     |         |
| out_input   | Stream for object.        | \[out\] |
| out_size    | Length of *`out_input`* . | \[out\] |
| cancellable | Cancellable               |         |
| error       | Error                     |         |

------------------------------------------------------------------------

### ostree_repo_query_object_storage_size ()

``` programlisting
gboolean
ostree_repo_query_object_storage_size (OstreeRepo *self,
                                       OstreeObjectType objtype,
                                       const char *sha256,
                                       guint64 *out_size,
                                       GCancellable *cancellable,
                                       GError **error);
```

Return the size in bytes of object with checksum *`sha256`* , after any compression has been applied.

#### Parameters

|             |                                           |         |
|-------------|-------------------------------------------|---------|
| self        | Repo                                      |         |
| objtype     | Object type                               |         |
| sha256      | Checksum                                  |         |
| out_size    | Size in bytes object occupies physically. | \[out\] |
| cancellable | Cancellable                               |         |
| error       | Error                                     |         |

------------------------------------------------------------------------

### ostree_repo_import_object_from ()

``` programlisting
gboolean
ostree_repo_import_object_from (OstreeRepo *self,
                                OstreeRepo *source,
                                OstreeObjectType objtype,
                                const char *checksum,
                                GCancellable *cancellable,
                                GError **error);
```

Copy object named by *`objtype`* and *`checksum`* into *`self`* from the source repository *`source`* . If both repositories are of the same type and on the same filesystem, this will simply be a fast Unix hard link operation.

Otherwise, a copy will be performed.

#### Parameters

|             |                  |     |
|-------------|------------------|-----|
| self        | Destination repo |     |
| source      | Source repo      |     |
| objtype     | Object type      |     |
| checksum    | checksum         |     |
| cancellable | Cancellable      |     |
| error       | Error            |     |

------------------------------------------------------------------------

### ostree_repo_import_object_from_with_trust ()

``` programlisting
gboolean
ostree_repo_import_object_from_with_trust
                               (OstreeRepo *self,
                                OstreeRepo *source,
                                OstreeObjectType objtype,
                                const char *checksum,
                                gboolean trusted,
                                GCancellable *cancellable,
                                GError **error);
```

Copy object named by *`objtype`* and *`checksum`* into *`self`* from the source repository *`source`* . If *`trusted`* is `TRUE` and both repositories are of the same type and on the same filesystem, this will simply be a fast Unix hard link operation.

Otherwise, a copy will be performed.

#### Parameters

|             |                                                        |     |
|-------------|--------------------------------------------------------|-----|
| self        | Destination repo                                       |     |
| source      | Source repo                                            |     |
| objtype     | Object type                                            |     |
| checksum    | checksum                                               |     |
| trusted     | If `TRUE`, assume the source repo is valid and trusted |     |
| cancellable | Cancellable                                            |     |
| error       | Error                                                  |     |

Since: 2016.5

------------------------------------------------------------------------

### ostree_repo_import_archive_to_mtree ()

``` programlisting
gboolean
ostree_repo_import_archive_to_mtree (OstreeRepo *self,
                                     OstreeRepoImportArchiveOptions *opts,
                                     void *archive,
                                     OstreeMutableTree *mtree,
                                     OstreeRepoCommitModifier *modifier,
                                     GCancellable *cancellable,
                                     GError **error);
```

Import an archive file *`archive`* into the repository, and write its file structure to *`mtree`* .

\[skip\]

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| opts | Options structure, ensure this is zeroed, then set specific variables |   |
| archive | Really this is "struct archive\*" |   |
| mtree | The [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") to write to |   |
| modifier | Optional commit modifier. | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_export_tree_to_archive ()

``` programlisting
gboolean
ostree_repo_export_tree_to_archive (OstreeRepo *self,
                                    OstreeRepoExportArchiveOptions *opts,
                                    OstreeRepoFile *root,
                                    void *archive,
                                    GCancellable *cancellable,
                                    GError **error);
```

Import an archive file *`archive`* into the repository, and write its file structure to *`mtree`* .

\[skip\]

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| opts | Options controlling conversion |   |
| root | An [OstreeRepoFile](reference__ostree-ostree-repo-file.md#OstreeRepoFile "OstreeRepoFile") for the base directory |   |
| archive | A `struct archive`, but specified as void to avoid a dependency on the libarchive headers |   |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_delete_object ()

``` programlisting
gboolean
ostree_repo_delete_object (OstreeRepo *self,
                           OstreeObjectType objtype,
                           const char *sha256,
                           GCancellable *cancellable,
                           GError **error);
```

Remove the object of type *`objtype`* with checksum *`sha256`* from the repository. An error of type `G_IO_ERROR_NOT_FOUND` is thrown if the object does not exist.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Repo        |     |
| objtype     | Object type |     |
| sha256      | Checksum    |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

------------------------------------------------------------------------

### ostree_repo_fsck_object ()

``` programlisting
gboolean
ostree_repo_fsck_object (OstreeRepo *self,
                         OstreeObjectType objtype,
                         const char *sha256,
                         GCancellable *cancellable,
                         GError **error);
```

Verify consistency of the object; this performs checks only relevant to the immediate object itself, such as checksumming. This API call will not itself traverse metadata objects for example.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Repo        |     |
| objtype     | Object type |     |
| sha256      | Checksum    |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

Since: 2017.15

------------------------------------------------------------------------

### OstreeRepoCommitFilter ()

``` programlisting
OstreeRepoCommitFilterResult
(*OstreeRepoCommitFilter) (OstreeRepo *repo,
                           const char *path,
                           GFileInfo *file_info,
                           gpointer user_data);
```

#### Parameters

|           |                  |     |
|-----------|------------------|-----|
| repo      | Repo             |     |
| path      | Path to file     |     |
| file_info | File information |     |
| user_data | User data        |     |

#### Returns

[OstreeRepoCommitFilterResult](reference__ostree-OstreeRepo.md#OstreeRepoCommitFilterResult "enum OstreeRepoCommitFilterResult") saying whether or not to commit this file

------------------------------------------------------------------------

### ostree_repo_commit_modifier_new ()

``` programlisting
OstreeRepoCommitModifier *
ostree_repo_commit_modifier_new (OstreeRepoCommitModifierFlags flags,
                                 OstreeRepoCommitFilter commit_filter,
                                 gpointer user_data,
                                 GDestroyNotify destroy_notify);
```

#### Parameters

|                |                                             |                |
|----------------|---------------------------------------------|----------------|
| flags          | Control options for filter                  |                |
| commit_filter  | Function that can inspect individual files. | \[allow-none\] |
| user_data      | User data.                                  | \[allow-none\] |
| destroy_notify | A GDestroyNotify                            |                |

#### Returns

A new commit modifier.

\[transfer full\]

------------------------------------------------------------------------

### OstreeRepoCommitModifierXattrCallback ()

``` programlisting
GVariant *
(*OstreeRepoCommitModifierXattrCallback)
                               (OstreeRepo *repo,
                                const char *path,
                                GFileInfo *file_info,
                                gpointer user_data);
```

------------------------------------------------------------------------

### ostree_repo_commit_modifier_set_xattr_callback ()

``` programlisting
void
ostree_repo_commit_modifier_set_xattr_callback
                               (OstreeRepoCommitModifier *modifier,
                                OstreeRepoCommitModifierXattrCallback callback,
                                GDestroyNotify destroy,
                                gpointer user_data);
```

If set, this function should return extended attributes to use for the given path. This is useful for things like ACLs and SELinux, where a build system can label the files as it's committing to the repository.

#### Parameters

|  |  |  |
|----|----|----|
| modifier | An [OstreeRepoCommitModifier](reference__ostree-OstreeRepo.md#OstreeRepoCommitModifier "OstreeRepoCommitModifier") |   |
| callback | Function to be invoked, should return extended attributes for path |   |
| destroy | Destroy notification |   |
| user_data | Data for *`callback`* : |   |

------------------------------------------------------------------------

### ostree_repo_commit_modifier_set_sepolicy ()

``` programlisting
void
ostree_repo_commit_modifier_set_sepolicy
                               (OstreeRepoCommitModifier *modifier,
                                OstreeSePolicy *sepolicy);
```

If *`policy`* is non-`NULL`, use it to look up labels to use for "security.selinux" extended attributes.

Note that any policy specified this way operates in addition to any extended attributes provided via [`ostree_repo_commit_modifier_set_xattr_callback()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-set-xattr-callback "ostree_repo_commit_modifier_set_xattr_callback ()"). However if both specify a value for "security.selinux", then the one from the policy wins.

#### Parameters

|  |  |  |
|----|----|----|
| modifier | An [OstreeRepoCommitModifier](reference__ostree-OstreeRepo.md#OstreeRepoCommitModifier "OstreeRepoCommitModifier") |   |
| sepolicy | Policy to use for labeling. | \[allow-none\] |

------------------------------------------------------------------------

### ostree_repo_commit_modifier_set_sepolicy_from_commit ()

``` programlisting
gboolean
ostree_repo_commit_modifier_set_sepolicy_from_commit
                               (OstreeRepoCommitModifier *modifier,
                                OstreeRepo *repo,
                                const char *rev,
                                GCancellable *cancellable,
                                GError **error);
```

In many cases, one wants to create a "derived" commit from base commit. SELinux policy labels are part of that base commit. This API allows one to easily set up SELinux labeling from a base commit.

#### Parameters

|          |                                           |     |
|----------|-------------------------------------------|-----|
| modifier | Commit modifier                           |     |
| repo     | OSTree repo containing *`rev`*            |     |
| rev      | Find SELinux policy from this base commit |     |

Since: 2020.4

------------------------------------------------------------------------

### ostree_repo_commit_modifier_set_devino_cache ()

``` programlisting
void
ostree_repo_commit_modifier_set_devino_cache
                               (OstreeRepoCommitModifier *modifier,
                                OstreeRepoDevInoCache *cache);
```

See the documentation for [`ostree_repo_devino_cache_new()`](reference__ostree-OstreeRepo.md#ostree-repo-devino-cache-new "ostree_repo_devino_cache_new ()"). This function can then be used for later calls to [`ostree_repo_write_directory_to_mtree()`](reference__ostree-OstreeRepo.md#ostree-repo-write-directory-to-mtree "ostree_repo_write_directory_to_mtree ()") to optimize commits.

Note if your process has multiple writers, you should use separate `OSTreeRepo` instances if you want to also use this API.

This function will add a reference to *`cache`* without copying - you should avoid further mutation of the cache.

#### Parameters

|          |                                                |     |
|----------|------------------------------------------------|-----|
| modifier | Modifier                                       |     |
| cache    | A hash table caching device,inode to checksums |     |

Since: 2017.13

------------------------------------------------------------------------

### ostree_repo_commit_modifier_ref ()

``` programlisting
OstreeRepoCommitModifier *
ostree_repo_commit_modifier_ref (OstreeRepoCommitModifier *modifier);
```

------------------------------------------------------------------------

### ostree_repo_commit_modifier_unref ()

``` programlisting
void
ostree_repo_commit_modifier_unref (OstreeRepoCommitModifier *modifier);
```

------------------------------------------------------------------------

### ostree_repo_devino_cache_new ()

``` programlisting
OstreeRepoDevInoCache *
ostree_repo_devino_cache_new (void);
```

OSTree has support for pairing [`ostree_repo_checkout_tree_at()`](reference__ostree-OstreeRepo.md#ostree-repo-checkout-tree-at "ostree_repo_checkout_tree_at ()") using hardlinks in combination with a later [`ostree_repo_write_directory_to_mtree()`](reference__ostree-OstreeRepo.md#ostree-repo-write-directory-to-mtree "ostree_repo_write_directory_to_mtree ()") using a (normally modified) directory. In order for OSTree to optimally detect just the new files, use this function and fill in the `devino_to_csum_cache` member of `OstreeRepoCheckoutAtOptions`, then call `ostree_repo_commit_set_devino_cache()`.

#### Returns

Newly allocated cache.

\[transfer full\]

------------------------------------------------------------------------

### ostree_repo_devino_cache_ref ()

``` programlisting
OstreeRepoDevInoCache *
ostree_repo_devino_cache_ref (OstreeRepoDevInoCache *cache);
```

------------------------------------------------------------------------

### ostree_repo_devino_cache_unref ()

``` programlisting
void
ostree_repo_devino_cache_unref (OstreeRepoDevInoCache *cache);
```

------------------------------------------------------------------------

### ostree_repo_devino_cache_get_type ()

``` programlisting
GType
ostree_repo_devino_cache_get_type (void);
```

------------------------------------------------------------------------

### ostree_repo_write_directory_to_mtree ()

``` programlisting
gboolean
ostree_repo_write_directory_to_mtree (OstreeRepo *self,
                                      GFile *dir,
                                      OstreeMutableTree *mtree,
                                      OstreeRepoCommitModifier *modifier,
                                      GCancellable *cancellable,
                                      GError **error);
```

Store objects for *`dir`* and all children into the repository *`self`* , overlaying the resulting filesystem hierarchy into *`mtree`* .

#### Parameters

|             |                                           |                |
|-------------|-------------------------------------------|----------------|
| self        | Repo                                      |                |
| dir         | Path to a directory                       |                |
| mtree       | Overlay directory contents into this tree |                |
| modifier    | Optional modifier.                        | \[allow-none\] |
| cancellable | Cancellable                               |                |
| error       | Error                                     |                |

------------------------------------------------------------------------

### ostree_repo_write_dfd_to_mtree ()

``` programlisting
gboolean
ostree_repo_write_dfd_to_mtree (OstreeRepo *self,
                                int dfd,
                                const char *path,
                                OstreeMutableTree *mtree,
                                OstreeRepoCommitModifier *modifier,
                                GCancellable *cancellable,
                                GError **error);
```

Store as objects all contents of the directory referred to by *`dfd`* and *`path`* all children into the repository *`self`* , overlaying the resulting filesystem hierarchy into *`mtree`* .

#### Parameters

|             |                                           |                |
|-------------|-------------------------------------------|----------------|
| self        | Repo                                      |                |
| dfd         | Directory file descriptor                 |                |
| path        | Path                                      |                |
| mtree       | Overlay directory contents into this tree |                |
| modifier    | Optional modifier.                        | \[allow-none\] |
| cancellable | Cancellable                               |                |
| error       | Error                                     |                |

------------------------------------------------------------------------

### ostree_repo_write_archive_to_mtree ()

``` programlisting
gboolean
ostree_repo_write_archive_to_mtree (OstreeRepo *self,
                                    GFile *archive,
                                    OstreeMutableTree *mtree,
                                    OstreeRepoCommitModifier *modifier,
                                    gboolean autocreate_parents,
                                    GCancellable *cancellable,
                                    GError **error);
```

Import an archive file *`archive`* into the repository, and write its file structure to *`mtree`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| archive | A path to an archive file |   |
| mtree | The [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") to write to |   |
| modifier | Optional commit modifier. | \[allow-none\] |
| autocreate_parents | Autocreate parent directories |   |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_write_archive_to_mtree_from_fd ()

``` programlisting
gboolean
ostree_repo_write_archive_to_mtree_from_fd
                               (OstreeRepo *self,
                                int fd,
                                OstreeMutableTree *mtree,
                                OstreeRepoCommitModifier *modifier,
                                gboolean autocreate_parents,
                                GCancellable *cancellable,
                                GError **error);
```

Read an archive from *`fd`* and import it into the repository, writing its file structure to *`mtree`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| fd | A file descriptor to read the archive from |   |
| mtree | The [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") to write to |   |
| modifier | Optional commit modifier. | \[allow-none\] |
| autocreate_parents | Autocreate parent directories |   |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_write_mtree ()

``` programlisting
gboolean
ostree_repo_write_mtree (OstreeRepo *self,
                         OstreeMutableTree *mtree,
                         GFile **out_file,
                         GCancellable *cancellable,
                         GError **error);
```

Write all metadata objects for *`mtree`* to repo; the resulting *`out_file`* points to the [`OSTREE_OBJECT_TYPE_DIR_TREE`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-DIR-TREE:CAPS) object that the *`mtree`* represented.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| mtree | Mutable tree |   |
| out_file | An [OstreeRepoFile](reference__ostree-ostree-repo-file.md#OstreeRepoFile "OstreeRepoFile") representing *`mtree`* 's root. | \[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_write_commit ()

``` programlisting
gboolean
ostree_repo_write_commit (OstreeRepo *self,
                          const char *parent,
                          const char *subject,
                          const char *body,
                          GVariant *metadata,
                          OstreeRepoFile *root,
                          char **out_commit,
                          GCancellable *cancellable,
                          GError **error);
```

Write a commit metadata object, referencing *`root_contents_checksum`* and *`root_metadata_checksum`* . This uses the current time as the commit timestamp, but it can be overridden with an explicit timestamp via the [standard](https://reproducible-builds.org/specs/source-date-epoch/) `SOURCE_DATE_EPOCH` environment flag.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| parent | ASCII SHA256 checksum for parent, or `NULL` for none. | \[nullable\] |
| subject | Subject. | \[nullable\] |
| body | Body. | \[nullable\] |
| metadata | GVariant of type a{sv}, or `NULL` for none. | \[nullable\] |
| root | The tree to point the commit to |   |
| out_commit | Resulting ASCII SHA256 checksum for commit. | \[out\]\[optional\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_write_commit_with_time ()

``` programlisting
gboolean
ostree_repo_write_commit_with_time (OstreeRepo *self,
                                    const char *parent,
                                    const char *subject,
                                    const char *body,
                                    GVariant *metadata,
                                    OstreeRepoFile *root,
                                    guint64 time,
                                    char **out_commit,
                                    GCancellable *cancellable,
                                    GError **error);
```

Write a commit metadata object, referencing *`root_contents_checksum`* and *`root_metadata_checksum`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| parent | ASCII SHA256 checksum for parent, or `NULL` for none. | \[nullable\] |
| subject | Subject. | \[nullable\] |
| body | Body. | \[nullable\] |
| metadata | GVariant of type a{sv}, or `NULL` for none. | \[nullable\] |
| root | The tree to point the commit to |   |
| time | The time to use to stamp the commit |   |
| out_commit | Resulting ASCII SHA256 checksum for commit. | \[out\]\[optional\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_read_commit_detached_metadata ()

``` programlisting
gboolean
ostree_repo_read_commit_detached_metadata
                               (OstreeRepo *self,
                                const char *checksum,
                                GVariant **out_metadata,
                                GCancellable *cancellable,
                                GError **error);
```

OSTree commits can have arbitrary metadata associated; this function retrieves them. If none exists, *`out_metadata`* will be set to `NULL`.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| checksum | ASCII SHA256 commit checksum |   |
| out_metadata | Metadata associated with commit in with format "a{sv}", or `NULL` if none exists. | \[out\]\[nullable\]\[transfer full\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_write_commit_detached_metadata ()

``` programlisting
gboolean
ostree_repo_write_commit_detached_metadata
                               (OstreeRepo *self,
                                const char *checksum,
                                GVariant *metadata,
                                GCancellable *cancellable,
                                GError **error);
```

Replace any existing metadata associated with commit referred to by *`checksum`* with *`metadata`* . If *`metadata`* is `NULL`, then existing data will be deleted.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| checksum | ASCII SHA256 commit checksum |   |
| metadata | Metadata to associate with commit in with format "a{sv}", or `NULL` to delete. | \[nullable\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_commit_add_composefs_metadata ()

``` programlisting
gboolean
ostree_repo_commit_add_composefs_metadata
                               (OstreeRepo *self,
                                guint format_version,
                                GVariantDict *dict,
                                OstreeRepoFile *repo_root,
                                GCancellable *cancellable,
                                GError **error);
```

Compute the composefs digest for a filesystem tree and insert it into metadata for a commit object. The composefs digest covers the entire filesystem tree and can be verified by the composefs mount tooling.

#### Parameters

|                |                                  |     |
|----------------|----------------------------------|-----|
| self           | Repo                             |     |
| format_version | Must be zero                     |     |
| dict           | A GVariant builder of type a{sv} |     |
| repo_root      | the target filesystem tree       |     |
| cancellable    | Cancellable                      |     |
| error          | Error                            |     |

------------------------------------------------------------------------

### ostree_repo_checkout_at_options_set_devino ()

``` programlisting
void
ostree_repo_checkout_at_options_set_devino
                               (OstreeRepoCheckoutAtOptions *opts,
                                OstreeRepoDevInoCache *cache);
```

This function simply assigns *`cache`* to the `devino_to_csum_cache` member of *`opts`* ; it's only useful for introspection.

Note that cache does \*not\* have its refcount incremented - the lifetime of *`cache`* must be equal to or greater than that of *`opts`* .

#### Parameters

|       |                  |                               |
|-------|------------------|-------------------------------|
| opts  | Checkout options |                               |
| cache | Devino cache.    | \[transfer none\]\[nullable\] |

Since: 2017.13

------------------------------------------------------------------------

### ostree_repo_checkout_tree ()

``` programlisting
gboolean
ostree_repo_checkout_tree (OstreeRepo *self,
                           OstreeRepoCheckoutMode mode,
                           OstreeRepoCheckoutOverwriteMode overwrite_mode,
                           GFile *destination,
                           OstreeRepoFile *source,
                           GFileInfo *source_info,
                           GCancellable *cancellable,
                           GError **error);
```

Check out *`source`* into *`destination`* , which must live on the physical filesystem. *`source`* may be any subdirectory of a given commit. The *`mode`* and *`overwrite_mode`* allow control over how the files are checked out.

#### Parameters

|                |                                   |     |
|----------------|-----------------------------------|-----|
| self           | Repo                              |     |
| mode           | Options controlling all files     |     |
| overwrite_mode | Whether or not to overwrite files |     |
| destination    | Place tree here                   |     |
| source         | Source tree                       |     |
| source_info    | Source info                       |     |
| cancellable    | Cancellable                       |     |
| error          | Error                             |     |

------------------------------------------------------------------------

### ostree_repo_checkout_tree_at ()

``` programlisting
gboolean
ostree_repo_checkout_tree_at (OstreeRepo *self,
                              OstreeRepoCheckoutOptions *options,
                              int destination_dfd,
                              const char *destination_path,
                              const char *commit,
                              GCancellable *cancellable,
                              GError **error);
```

`ostree_repo_checkout_tree_at` is deprecated and should not be used in newly-written code.

Similar to [`ostree_repo_checkout_tree()`](reference__ostree-OstreeRepo.md#ostree-repo-checkout-tree "ostree_repo_checkout_tree ()"), but uses directory-relative paths for the destination, uses a new `OstreeRepoCheckoutAtOptions`, and takes a commit checksum and optional subpath pair, rather than requiring use of `GFile` APIs for the caller.

Note in addition that unlike [`ostree_repo_checkout_tree()`](reference__ostree-OstreeRepo.md#ostree-repo-checkout-tree "ostree_repo_checkout_tree ()"), the default is not to use the repository-internal uncompressed objects cache.

This function is deprecated. Use [`ostree_repo_checkout_at()`](reference__ostree-OstreeRepo.md#ostree-repo-checkout-at "ostree_repo_checkout_at ()") instead.

\[skip\]

#### Parameters

|                  |                              |                |
|------------------|------------------------------|----------------|
| self             | Repo                         |                |
| options          | Options.                     | \[allow-none\] |
| destination_dfd  | Directory FD for destination |                |
| destination_path | Directory for destination    |                |
| commit           | Checksum for commit          |                |
| cancellable      | Cancellable                  |                |
| error            | Error                        |                |

------------------------------------------------------------------------

### ostree_repo_checkout_at ()

``` programlisting
gboolean
ostree_repo_checkout_at (OstreeRepo *self,
                         OstreeRepoCheckoutAtOptions *options,
                         int destination_dfd,
                         const char *destination_path,
                         const char *commit,
                         GCancellable *cancellable,
                         GError **error);
```

Similar to [`ostree_repo_checkout_tree()`](reference__ostree-OstreeRepo.md#ostree-repo-checkout-tree "ostree_repo_checkout_tree ()"), but uses directory-relative paths for the destination, uses a new `OstreeRepoCheckoutAtOptions`, and takes a commit checksum and optional subpath pair, rather than requiring use of `GFile` APIs for the caller.

It also replaces [`ostree_repo_checkout_at()`](reference__ostree-OstreeRepo.md#ostree-repo-checkout-at "ostree_repo_checkout_at ()") which was not safe to use with GObject introspection.

Note in addition that unlike [`ostree_repo_checkout_tree()`](reference__ostree-OstreeRepo.md#ostree-repo-checkout-tree "ostree_repo_checkout_tree ()"), the default is not to use the repository-internal uncompressed objects cache.

#### Parameters

|                  |                              |                |
|------------------|------------------------------|----------------|
| self             | Repo                         |                |
| options          | Options.                     | \[allow-none\] |
| destination_dfd  | Directory FD for destination |                |
| destination_path | Directory for destination    |                |
| commit           | Checksum for commit          |                |
| cancellable      | Cancellable                  |                |
| error            | Error                        |                |

Since: 2016.8

------------------------------------------------------------------------

### ostree_repo_checkout_composefs ()

``` programlisting
gboolean
ostree_repo_checkout_composefs (OstreeRepo *self,
                                GVariant *options,
                                int destination_dfd,
                                const char *destination_path,
                                const char *checksum,
                                GCancellable *cancellable,
                                GError **error);
```

Create a composefs filesystem metadata blob from an OSTree commit. Supported options:

- verity: `u`: 0 = disabled, 1 = set if present on file, 2 = enabled; any other value is a fatal error

#### Parameters

|  |  |  |
|----|----|----|
| self | A repo |   |
| options | If non-NULL, must be a GVariant of type a{sv}. See below. | \[nullable\] |
| destination_dfd | Parent directory fd |   |
| destination_path | Filename |   |
| checksum | OStree commit digest |   |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2024.7

------------------------------------------------------------------------

### ostree_repo_checkout_gc ()

``` programlisting
gboolean
ostree_repo_checkout_gc (OstreeRepo *self,
                         GCancellable *cancellable,
                         GError **error);
```

Call this after finishing a succession of checkout operations; it will delete any currently-unused uncompressed objects from the cache.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Repo        |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

------------------------------------------------------------------------

### ostree_repo_read_commit ()

``` programlisting
gboolean
ostree_repo_read_commit (OstreeRepo *self,
                         const char *ref,
                         GFile **out_root,
                         char **out_commit,
                         GCancellable *cancellable,
                         GError **error);
```

Load the content for *`rev`* into *`out_root`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| ref | Ref or ASCII checksum |   |
| out_root | An [OstreeRepoFile](reference__ostree-ostree-repo-file.md#OstreeRepoFile "OstreeRepoFile") corresponding to the root. | \[out\]\[optional\] |
| out_commit | The resolved commit checksum. | \[out\]\[optional\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_list_objects ()

``` programlisting
gboolean
ostree_repo_list_objects (OstreeRepo *self,
                          OstreeRepoListObjectsFlags flags,
                          GHashTable **out_objects,
                          GCancellable *cancellable,
                          GError **error);
```

This function synchronously enumerates all objects in the repository, returning data in *`out_objects`* . *`out_objects`* maps from keys returned by [`ostree_object_name_serialize()`](reference__ostree-Core-repository-independent-functions.md#ostree-object-name-serialize "ostree_object_name_serialize ()") to GVariant values of type [`OSTREE_REPO_LIST_OBJECTS_VARIANT_TYPE`](reference__ostree-OstreeRepo.md#OSTREE-REPO-LIST-OBJECTS-VARIANT-TYPE:CAPS "OSTREE_REPO_LIST_OBJECTS_VARIANT_TYPE").

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| flags | Flags controlling enumeration |   |
| out_objects | Map of serialized object name to variant data. | \[out\]\[transfer container\]\[element-type GVariant GVariant\] |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

`TRUE` on success, `FALSE` on error, and *`error`* will be set

------------------------------------------------------------------------

### ostree_repo_list_commit_objects_starting_with ()

``` programlisting
gboolean
ostree_repo_list_commit_objects_starting_with
                               (OstreeRepo *self,
                                const char *start,
                                GHashTable **out_commits,
                                GCancellable *cancellable,
                                GError **error);
```

This function synchronously enumerates all commit objects starting with *`start`* , returning data in *`out_commits`* .

To list all commit objects, provide the empty string `""` for *`start`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| start | List commits starting with this checksum (empty string for all) |   |
| out_commits | Map of serialized commit name to variant data. | \[out\]\[transfer container\]\[element-type GVariant GVariant\] |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

`TRUE` on success, `FALSE` on error, and *`error`* will be set

------------------------------------------------------------------------

### ostree_repo_list_static_delta_names ()

``` programlisting
gboolean
ostree_repo_list_static_delta_names (OstreeRepo *self,
                                     GPtrArray **out_deltas,
                                     GCancellable *cancellable,
                                     GError **error);
```

This function synchronously enumerates all static deltas in the repository, returning its result in *`out_deltas`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| out_deltas | String name of deltas (checksum-checksum.delta). | \[out\]\[element-type utf8\]\[transfer container\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_list_static_delta_indexes ()

``` programlisting
gboolean
ostree_repo_list_static_delta_indexes (OstreeRepo *self,
                                       GPtrArray **out_indexes,
                                       GCancellable *cancellable,
                                       GError **error);
```

This function synchronously enumerates all static delta indexes in the repository, returning its result in *`out_indexes`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| out_indexes | String name of delta indexes (checksum). | \[out\]\[element-type utf8\]\[transfer container\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2020.8

------------------------------------------------------------------------

### ostree_repo_static_delta_reindex ()

``` programlisting
gboolean
ostree_repo_static_delta_reindex (OstreeRepo *repo,
                                  OstreeStaticDeltaIndexFlags flags,
                                  const char *opt_to_commit,
                                  GCancellable *cancellable,
                                  GError **error);
```

The delta index for a particular commit lists all the existing deltas that can be used when downloading that commit. This operation regenerates these indexes, either for a particular commit (if *`opt_to_commit`* is non-`NULL`), or for all commits that are reachable by an existing delta (if *`opt_to_commit`* is `NULL`).

This is normally called automatically when the summary is updated in [`ostree_repo_regenerate_summary()`](reference__ostree-OstreeRepo.md#ostree-repo-regenerate-summary "ostree_repo_regenerate_summary ()").

Locking: shared

#### Parameters

|  |  |  |
|----|----|----|
| repo | Repo |   |
| flags | Flags affecting the indexing operation |   |
| opt_to_commit | ASCII SHA256 checksum of target commit, or `NULL` to index all targets |   |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2020.8

------------------------------------------------------------------------

### ostree_repo_static_delta_generate ()

``` programlisting
gboolean
ostree_repo_static_delta_generate (OstreeRepo *self,
                                   OstreeStaticDeltaGenerateOpt opt,
                                   const char *from,
                                   const char *to,
                                   GVariant *metadata,
                                   GVariant *params,
                                   GCancellable *cancellable,
                                   GError **error);
```

Generate a lookaside "static delta" from *`from`* (`NULL` means from-empty) which can generate the objects in *`to`* . This delta is an optimization over fetching individual objects, and can be conveniently stored and applied offline.

The *`params`* argument should be an a{sv}. The following attributes are known:

- min-fallback-size: u: Minimum uncompressed size in megabytes to use fallback, 0 to disable fallbacks

- max-chunk-size: u: Maximum size in megabytes of a delta part

- max-bsdiff-size: u: Maximum size in megabytes to consider bsdiff compression for input files

- compression: y: Compression type: 0=none, x=lzma, g=gzip

- bsdiff-enabled: b: Enable bsdiff compression. Default TRUE.

- inline-parts: b: Put part data in header, to get a single file delta. Default FALSE.

- verbose: b: Print diagnostic messages. Default FALSE.

- endianness: b: Deltas use host byte order by default; this option allows choosing (G_BIG_ENDIAN or G_LITTLE_ENDIAN)

- filename: ^ay: Save delta superblock to this filename (bytestring), and parts in the same directory. Default saves to repository.

- sign-name: ^ay: Signature type to use (bytestring).

- sign-key-ids: ^as: NULL-terminated array of keys used to sign delta superblock.

#### Parameters

|             |                                             |              |
|-------------|---------------------------------------------|--------------|
| self        | Repo                                        |              |
| opt         | High level optimization choice              |              |
| from        | ASCII SHA256 checksum of origin, or `NULL`. | \[nullable\] |
| to          | ASCII SHA256 checksum of target             |              |
| metadata    | Optional metadata.                          | \[nullable\] |
| params      | Parameters, see below.                      | \[nullable\] |
| cancellable | Cancellable                                 |              |
| error       | Error                                       |              |

------------------------------------------------------------------------

### ostree_repo_static_delta_execute_offline_with_signature ()

``` programlisting
gboolean
ostree_repo_static_delta_execute_offline_with_signature
                               (OstreeRepo *self,
                                GFile *dir_or_file,
                                OstreeSign *sign,
                                gboolean skip_validation,
                                GCancellable *cancellable,
                                GError **error);
```

Given a directory representing an already-downloaded static delta on disk, apply it, generating a new commit. If sign is passed, the static delta signature is verified. If sign-verify-deltas configuration option is set and static delta is signed, signature verification will be mandatory before apply the static delta. The directory must be named with the form "FROM-TO", where both are checksums, and it must contain a file named "superblock", along with at least one part.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| dir_or_file | Path to a directory containing static delta data, or directly to the superblock |   |
| sign | Signature engine used to check superblock |   |
| skip_validation | If `TRUE`, assume data integrity |   |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2020.7

------------------------------------------------------------------------

### ostree_repo_static_delta_execute_offline ()

``` programlisting
gboolean
ostree_repo_static_delta_execute_offline
                               (OstreeRepo *self,
                                GFile *dir_or_file,
                                gboolean skip_validation,
                                GCancellable *cancellable,
                                GError **error);
```

Given a directory representing an already-downloaded static delta on disk, apply it, generating a new commit. The directory must be named with the form "FROM-TO", where both are checksums, and it must contain a file named "superblock", along with at least one part.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| dir_or_file | Path to a directory containing static delta data, or directly to the superblock |   |
| skip_validation | If `TRUE`, assume data integrity |   |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_static_delta_verify_signature ()

``` programlisting
gboolean
ostree_repo_static_delta_verify_signature
                               (OstreeRepo *self,
                                const char *delta_id,
                                OstreeSign *sign,
                                char **out_success_message,
                                GError **error);
```

Verify static delta file signature.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| delta_id | delta path |   |
| sign | Signature engine used to check superblock |   |
| out_success_message | success message. | \[out\]\[nullable\]\[optional\] |
| error | Error |   |

#### Returns

TRUE if the signature of static delta file is valid using the signature engine provided, FALSE otherwise.

Since: 2020.7

------------------------------------------------------------------------

### ostree_repo_traverse_new_reachable ()

``` programlisting
GHashTable *
ostree_repo_traverse_new_reachable (void);
```

This hash table is a set of GVariant which can be accessed via [`ostree_object_name_deserialize()`](reference__ostree-Core-repository-independent-functions.md#ostree-object-name-deserialize "ostree_object_name_deserialize ()").

#### Returns

A new hash table.

\[transfer container\]\[element-type GVariant GVariant\]

------------------------------------------------------------------------

### ostree_repo_traverse_new_parents ()

``` programlisting
GHashTable *
ostree_repo_traverse_new_parents (void);
```

This hash table is a mapping from GVariant which can be accessed via [`ostree_object_name_deserialize()`](reference__ostree-Core-repository-independent-functions.md#ostree-object-name-deserialize "ostree_object_name_deserialize ()") to a GVariant containing either a similar GVariant or and array of them, listing the parents of the key.

#### Returns

A new hash table.

\[transfer container\]\[element-type GVariant GVariant\]

Since: 2018.5

------------------------------------------------------------------------

### ostree_repo_traverse_parents_get_commits ()

``` programlisting
char **
ostree_repo_traverse_parents_get_commits
                               (GHashTable *parents,
                                GVariant *object);
```

Gets all the commits that a certain object belongs to, as recorded by a parents table gotten from ostree_repo_traverse_commit_union_with_parents.

#### Returns

An array of checksums for the commits the key belongs to.

\[transfer full\]\[array zero-terminated=1\]

Since: 2018.5

------------------------------------------------------------------------

### ostree_repo_traverse_commit ()

``` programlisting
gboolean
ostree_repo_traverse_commit (OstreeRepo *repo,
                             const char *commit_checksum,
                             int maxdepth,
                             GHashTable **out_reachable,
                             GCancellable *cancellable,
                             GError **error);
```

Create a new set *`out_reachable`* containing all objects reachable from *`commit_checksum`* , traversing *`maxdepth`* parent commits.

#### Parameters

|  |  |  |
|----|----|----|
| repo | Repo |   |
| commit_checksum | ASCII SHA256 checksum |   |
| maxdepth | Traverse this many parent commits, -1 for unlimited |   |
| out_reachable | Set of reachable objects. | \[out\]\[transfer container\]\[element-type GVariant GVariant\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_traverse_commit_union ()

``` programlisting
gboolean
ostree_repo_traverse_commit_union (OstreeRepo *repo,
                                   const char *commit_checksum,
                                   int maxdepth,
                                   GHashTable *inout_reachable,
                                   GCancellable *cancellable,
                                   GError **error);
```

Update the set *`inout_reachable`* containing all objects reachable from *`commit_checksum`* , traversing *`maxdepth`* parent commits.

\[skip\]

#### Parameters

|                 |                                                     |     |
|-----------------|-----------------------------------------------------|-----|
| repo            | Repo                                                |     |
| commit_checksum | ASCII SHA256 checksum                               |     |
| maxdepth        | Traverse this many parent commits, -1 for unlimited |     |
| inout_reachable | Set of reachable objects                            |     |
| cancellable     | Cancellable                                         |     |
| error           | Error                                               |     |

------------------------------------------------------------------------

### ostree_repo_traverse_commit_union_with_parents ()

``` programlisting
gboolean
ostree_repo_traverse_commit_union_with_parents
                               (OstreeRepo *repo,
                                const char *commit_checksum,
                                int maxdepth,
                                GHashTable *inout_reachable,
                                GHashTable *inout_parents,
                                GCancellable *cancellable,
                                GError **error);
```

Update the set *`inout_reachable`* containing all objects reachable from *`commit_checksum`* , traversing *`maxdepth`* parent commits.

Additionally this constructs a mapping from each object to the parents of the object, which can be used to track which commits an object belongs to.

\[skip\]

#### Parameters

|                 |                                                     |     |
|-----------------|-----------------------------------------------------|-----|
| repo            | Repo                                                |     |
| commit_checksum | ASCII SHA256 checksum                               |     |
| maxdepth        | Traverse this many parent commits, -1 for unlimited |     |
| inout_reachable | Set of reachable objects                            |     |
| inout_parents   | Map from object to parent object                    |     |
| cancellable     | Cancellable                                         |     |
| error           | Error                                               |     |

Since: 2018.5

------------------------------------------------------------------------

### ostree_repo_traverse_commit_with_flags ()

``` programlisting
gboolean
ostree_repo_traverse_commit_with_flags
                               (OstreeRepo *repo,
                                OstreeRepoCommitTraverseFlags flags,
                                const char *commit_checksum,
                                int maxdepth,
                                GHashTable *inout_reachable,
                                GHashTable *inout_parents,
                                GCancellable *cancellable,
                                GError **error);
```

Update the set *`inout_reachable`* containing all objects reachable from *`commit_checksum`* , traversing *`maxdepth`* parent commits.

Additionally this constructs a mapping from each object to the parents of the object, which can be used to track which commits an object belongs to.

\[skip\]

#### Parameters

|                 |                                                     |     |
|-----------------|-----------------------------------------------------|-----|
| repo            | Repo                                                |     |
| flags           | change traversal behaviour according to these flags |     |
| commit_checksum | ASCII SHA256 checksum                               |     |
| maxdepth        | Traverse this many parent commits, -1 for unlimited |     |
| inout_reachable | Set of reachable objects                            |     |
| inout_parents   | Map from object to parent object                    |     |
| cancellable     | Cancellable                                         |     |
| error           | Error                                               |     |

Since: 2018.5

------------------------------------------------------------------------

### ostree_repo_commit_traverse_iter_cleanup ()

``` programlisting
void
ostree_repo_commit_traverse_iter_cleanup
                               (void *p);
```

------------------------------------------------------------------------

### ostree_repo_commit_traverse_iter_clear ()

``` programlisting
void
ostree_repo_commit_traverse_iter_clear
                               (OstreeRepoCommitTraverseIter *iter);
```

------------------------------------------------------------------------

### ostree_repo_commit_traverse_iter_get_dir ()

``` programlisting
void
ostree_repo_commit_traverse_iter_get_dir
                               (OstreeRepoCommitTraverseIter *iter,
                                char **out_name,
                                char **out_content_checksum,
                                char **out_meta_checksum);
```

Return information on the current directory. This function may only be called if [`OSTREE_REPO_COMMIT_ITER_RESULT_DIR`](reference__ostree-OstreeRepo.md#OSTREE-REPO-COMMIT-ITER-RESULT-DIR:CAPS) was returned from [`ostree_repo_commit_traverse_iter_next()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-next "ostree_repo_commit_traverse_iter_next ()").

#### Parameters

|  |  |  |
|----|----|----|
| iter | An iter |   |
| out_name | Name of current dir. | \[out\]\[transfer none\] |
| out_content_checksum | Checksum of current content. | \[out\]\[transfer none\] |
| out_meta_checksum | Checksum of current metadata. | \[out\]\[transfer none\] |

------------------------------------------------------------------------

### ostree_repo_commit_traverse_iter_get_file ()

``` programlisting
void
ostree_repo_commit_traverse_iter_get_file
                               (OstreeRepoCommitTraverseIter *iter,
                                char **out_name,
                                char **out_checksum);
```

Return information on the current file. This function may only be called if [`OSTREE_REPO_COMMIT_ITER_RESULT_FILE`](reference__ostree-OstreeRepo.md#OSTREE-REPO-COMMIT-ITER-RESULT-FILE:CAPS) was returned from [`ostree_repo_commit_traverse_iter_next()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-next "ostree_repo_commit_traverse_iter_next ()").

#### Parameters

|              |                           |                          |
|--------------|---------------------------|--------------------------|
| iter         | An iter                   |                          |
| out_name     | Name of current file.     | \[out\]\[transfer none\] |
| out_checksum | Checksum of current file. | \[out\]\[transfer none\] |

------------------------------------------------------------------------

### ostree_repo_commit_traverse_iter_init_commit ()

``` programlisting
gboolean
ostree_repo_commit_traverse_iter_init_commit
                               (OstreeRepoCommitTraverseIter *iter,
                                OstreeRepo *repo,
                                GVariant *commit,
                                OstreeRepoCommitTraverseFlags flags,
                                GError **error);
```

Initialize (in place) an iterator over the root of a commit object.

#### Parameters

|  |  |  |
|----|----|----|
| iter | An iter |   |
| repo | A repo |   |
| commit | Variant of type [`OSTREE_OBJECT_TYPE_COMMIT`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-COMMIT:CAPS) |   |
| flags | Flags |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_commit_traverse_iter_init_dirtree ()

``` programlisting
gboolean
ostree_repo_commit_traverse_iter_init_dirtree
                               (OstreeRepoCommitTraverseIter *iter,
                                OstreeRepo *repo,
                                GVariant *dirtree,
                                OstreeRepoCommitTraverseFlags flags,
                                GError **error);
```

Initialize (in place) an iterator over a directory tree.

#### Parameters

|  |  |  |
|----|----|----|
| iter | An iter |   |
| repo | A repo |   |
| dirtree | Variant of type [`OSTREE_OBJECT_TYPE_DIR_TREE`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-DIR-TREE:CAPS) |   |
| flags | Flags |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_commit_traverse_iter_next ()

``` programlisting
OstreeRepoCommitIterResult
ostree_repo_commit_traverse_iter_next (OstreeRepoCommitTraverseIter *iter,
                                       GCancellable *cancellable,
                                       GError **error);
```

Step the interator to the next item. Files will be returned first, then subdirectories. Call this in a loop; upon encountering [`OSTREE_REPO_COMMIT_ITER_RESULT_END`](reference__ostree-OstreeRepo.md#OSTREE-REPO-COMMIT-ITER-RESULT-END:CAPS), there will be no more files or directories. If [`OSTREE_REPO_COMMIT_ITER_RESULT_DIR`](reference__ostree-OstreeRepo.md#OSTREE-REPO-COMMIT-ITER-RESULT-DIR:CAPS) is returned, then call [`ostree_repo_commit_traverse_iter_get_dir()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-get-dir "ostree_repo_commit_traverse_iter_get_dir ()") to retrieve data for that directory. Similarly, if [`OSTREE_REPO_COMMIT_ITER_RESULT_FILE`](reference__ostree-OstreeRepo.md#OSTREE-REPO-COMMIT-ITER-RESULT-FILE:CAPS) is returned, call [`ostree_repo_commit_traverse_iter_get_file()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-get-file "ostree_repo_commit_traverse_iter_get_file ()").

If [`OSTREE_REPO_COMMIT_ITER_RESULT_ERROR`](reference__ostree-OstreeRepo.md#OSTREE-REPO-COMMIT-ITER-RESULT-ERROR:CAPS) is returned, it is a program error to call any further API on *`iter`* except for [`ostree_repo_commit_traverse_iter_clear()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-traverse-iter-clear "ostree_repo_commit_traverse_iter_clear ()").

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| iter        | An iter     |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

------------------------------------------------------------------------

### ostree_repo_prune ()

``` programlisting
gboolean
ostree_repo_prune (OstreeRepo *self,
                   OstreeRepoPruneFlags flags,
                   gint depth,
                   gint *out_objects_total,
                   gint *out_objects_pruned,
                   guint64 *out_pruned_object_size_total,
                   GCancellable *cancellable,
                   GError **error);
```

Delete content from the repository. By default, this function will only delete "orphaned" objects not referred to by any commit. This can happen during a local commit operation, when we have written content objects but not saved the commit referencing them.

However, if [`OSTREE_REPO_PRUNE_FLAGS_REFS_ONLY`](reference__ostree-OstreeRepo.md#OSTREE-REPO-PRUNE-FLAGS-REFS-ONLY:CAPS) is provided, instead of traversing all commits, only refs will be used. Particularly when combined with *`depth`* , this is a convenient way to delete history from the repository.

Use the [`OSTREE_REPO_PRUNE_FLAGS_NO_PRUNE`](reference__ostree-OstreeRepo.md#OSTREE-REPO-PRUNE-FLAGS-NO-PRUNE:CAPS) to just determine statistics on objects that would be deleted, without actually deleting them.

Locking: exclusive

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| flags | Options controlling prune process |   |
| depth | Stop traversal after this many iterations (-1 for unlimited) |   |
| out_objects_total | Number of objects found. | \[out\] |
| out_objects_pruned | Number of objects deleted. | \[out\] |
| out_pruned_object_size_total | Storage size in bytes of objects deleted. | \[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_prune_static_deltas ()

``` programlisting
gboolean
ostree_repo_prune_static_deltas (OstreeRepo *self,
                                 const char *commit,
                                 GCancellable *cancellable,
                                 GError **error);
```

Prune static deltas, if COMMIT is specified then delete static delta files only targeting that commit; otherwise any static delta of non existing commits are deleted.

Locking: exclusive

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| commit | ASCII SHA256 checksum for commit, or `NULL` for each non existing commit. | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_traverse_reachable_refs ()

``` programlisting
gboolean
ostree_repo_traverse_reachable_refs (OstreeRepo *self,
                                     guint depth,
                                     GHashTable *reachable,
                                     GCancellable *cancellable,
                                     GError **error);
```

Add all commit objects directly reachable via a ref to *`reachable`* .

Locking: shared

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| depth | Depth of traversal |   |
| reachable | Set of reachable objects (will be modified). | \[element-type GVariant GVariant\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_prune_from_reachable ()

``` programlisting
gboolean
ostree_repo_prune_from_reachable (OstreeRepo *self,
                                  OstreeRepoPruneOptions *options,
                                  gint *out_objects_total,
                                  gint *out_objects_pruned,
                                  guint64 *out_pruned_object_size_total,
                                  GCancellable *cancellable,
                                  GError **error);
```

Delete content from the repository. This function is the "backend" half of the higher level [`ostree_repo_prune()`](reference__ostree-OstreeRepo.md#ostree-repo-prune "ostree_repo_prune ()"). To use this function, you determine the root set yourself, and this function finds all other unreferenced objects and deletes them.

Use this API when you want to perform more selective pruning - for example, retain all commits from a production branch, but just GC some history from your dev branch.

The [`OSTREE_REPO_PRUNE_FLAGS_NO_PRUNE`](reference__ostree-OstreeRepo.md#OSTREE-REPO-PRUNE-FLAGS-NO-PRUNE:CAPS) flag may be specified to just determine statistics on objects that would be deleted, without actually deleting them.

Locking: exclusive

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| options | Options controlling prune process |   |
| out_objects_total | Number of objects found. | \[out\] |
| out_objects_pruned | Number of objects deleted. | \[out\] |
| out_pruned_object_size_total | Storage size in bytes of objects deleted. | \[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2017.1

------------------------------------------------------------------------

### ostree_repo_pull ()

``` programlisting
gboolean
ostree_repo_pull (OstreeRepo *self,
                  const char *remote_name,
                  char **refs_to_fetch,
                  OstreeRepoPullFlags flags,
                  OstreeAsyncProgress *progress,
                  GCancellable *cancellable,
                  GError **error);
```

Connect to the remote repository, fetching the specified set of refs *`refs_to_fetch`* . For each ref that is changed, download the commit, all metadata, and all content objects, storing them safely on disk in *`self`* .

If *`flags`* contains [`OSTREE_REPO_PULL_FLAGS_MIRROR`](reference__ostree-OstreeRepo.md#OSTREE-REPO-PULL-FLAGS-MIRROR:CAPS), and the *`refs_to_fetch`* is `NULL`, and the remote repository contains a summary file, then all refs will be fetched.

If *`flags`* contains [`OSTREE_REPO_PULL_FLAGS_COMMIT_ONLY`](reference__ostree-OstreeRepo.md#OSTREE-REPO-PULL-FLAGS-COMMIT-ONLY:CAPS), then only the metadata for the commits in *`refs_to_fetch`* is pulled.

Warning: This API will iterate the thread default main context, which is a bug, but kept for compatibility reasons. If you want to avoid this, use `g_main_context_push_thread_default()` to push a new one around this call.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| remote_name | Name of remote |   |
| refs_to_fetch | Optional list of refs; if `NULL`, fetch all configured refs. | \[array zero-terminated=1\]\[element-type utf8\]\[allow-none\] |
| flags | Options controlling fetch behavior |   |
| progress | Progress. | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_pull_one_dir ()

``` programlisting
gboolean
ostree_repo_pull_one_dir (OstreeRepo *self,
                          const char *remote_name,
                          const char *dir_to_pull,
                          char **refs_to_fetch,
                          OstreeRepoPullFlags flags,
                          OstreeAsyncProgress *progress,
                          GCancellable *cancellable,
                          GError **error);
```

This is similar to [`ostree_repo_pull()`](reference__ostree-OstreeRepo.md#ostree-repo-pull "ostree_repo_pull ()"), but only fetches a single subpath.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| remote_name | Name of remote |   |
| dir_to_pull | Subdirectory path |   |
| refs_to_fetch | Optional list of refs; if `NULL`, fetch all configured refs. | \[array zero-terminated=1\]\[element-type utf8\]\[allow-none\] |
| flags | Options controlling fetch behavior |   |
| progress | Progress. | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_pull_with_options ()

``` programlisting
gboolean
ostree_repo_pull_with_options (OstreeRepo *self,
                               const char *remote_name_or_baseurl,
                               GVariant *options,
                               OstreeAsyncProgress *progress,
                               GCancellable *cancellable,
                               GError **error);
```

Like [`ostree_repo_pull()`](reference__ostree-OstreeRepo.md#ostree-repo-pull "ostree_repo_pull ()"), but supports an extensible set of flags. The following are currently defined:

- `refs` (`as`): Array of string refs

- `collection-refs` (`a(sss)`): Array of (collection ID, ref name, checksum) tuples to pull; mutually exclusive with `refs` and `override-commit-ids`. Checksums may be the empty string to pull the latest commit for that ref

- `flags` (`i`): An instance of [OstreeRepoPullFlags](reference__ostree-OstreeRepo.md#OstreeRepoPullFlags "enum OstreeRepoPullFlags")

- `subdir` (`s`): Pull just this subdirectory

- `subdirs` (`as`): Pull just these subdirectories

- `override-remote-name` (`s`): If local, add this remote to refspec

- `gpg-verify` (`b`): GPG verify commits

- `gpg-verify-summary` (`b`): GPG verify summary

- `disable-sign-verify` (`b`): Disable signapi verification of commits

- `disable-sign-verify-summary` (`b`): Disable signapi verification of the summary

- `depth` (`i`): How far in the history to traverse; default is 0, -1 means infinite

- `per-object-fsync` (`b`): Perform disk writes more slowly, avoiding a single large I/O sync

- `disable-static-deltas` (`b`): Do not use static deltas

- `require-static-deltas` (`b`): Require static deltas

- `override-commit-ids` (`as`): Array of specific commit IDs to fetch for refs

- `timestamp-check` (`b`): Verify commit timestamps are newer than current (when pulling via ref); Since: 2017.11

- `timestamp-check-from-rev` (`s`): Verify that all fetched commit timestamps are newer than timestamp of given rev; Since: 2020.4

- `max-metadata-size` (`t`): Restrict metadata objects to a maximum number of bytes; 0 to disable. Since: 2018.9

- `dry-run` (`b`): Only print information on what will be downloaded (requires static deltas)

- `override-url` (`s`): Fetch objects from this URL if remote specifies no metalink in options

- `inherit-transaction` (`b`): Don't initiate, finish or abort a transaction, useful to do multiple pulls in one transaction.

- `http-headers` (`a(ss)`): Additional headers to add to all HTTP requests

- `update-frequency` (`u`): Frequency to call the async progress callback in milliseconds, if any; only values higher than 0 are valid

- `localcache-repos` (`as`): File paths for local repos to use as caches when doing remote fetches

- `append-user-agent` (`s`): Additional string to append to the user agent

- `n-network-retries` (`u`): Number of times to retry each download on receiving a transient network error, such as a socket timeout; default is 5, 0 means return errors without retrying. Since: 2018.6

- `low-speed-limit-bytes` (`u`): The average transfer speed per second of a transfer during the time set via "low-speed-time-seconds" for libcurl to abort.

- `low-speed-time-seconds` (`u`): The time in number seconds that the transfer speed should be below the "low-speed-limit-bytes" setting for libcurl to abort.

- `retry-all-network-errors` (`b`): Retry when network issues happen, instead of failing automatically. Currently only affects libcurl. (Default set to true)

- `max-outstanding-fetcher-requests` (`u`): The max amount of concurrent connections allowed.

- `ref-keyring-map` (`a(sss)`): Array of (collection ID, ref name, keyring remote name) tuples specifying which remote's keyring should be used when doing GPG verification of each collection-ref. This is useful to prevent a remote from serving malicious updates to refs which did not originate from it. This can be a subset or superset of the refs being pulled; any ref not being pulled will be ignored and any ref without a keyring remote will be verified with the keyring of the remote being pulled from.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| remote_name_or_baseurl | Name of remote or file:// url |   |
| options | A GVariant a{sv} with an extensible set of flags. |   |
| progress | Progress. | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2020.9

------------------------------------------------------------------------

### ostree_repo_pull_default_console_progress_changed ()

``` programlisting
void
ostree_repo_pull_default_console_progress_changed
                               (OstreeAsyncProgress *progress,
                                gpointer user_data);
```

Convenient "changed" callback for use with [`ostree_async_progress_new_and_connect()`](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-new-and-connect "ostree_async_progress_new_and_connect ()") when pulling from a remote repository.

Depending on the state of the [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress"), either displays a custom status message, or else outstanding fetch progress in bytes/sec, or else outstanding content or metadata writes to the repository in number of objects.

Compatibility note: this function previously assumed that *`user_data`* was a pointer to a GSConsole instance. This is no longer the case, and *`user_data`* is ignored.

#### Parameters

|           |                |                |
|-----------|----------------|----------------|
| progress  | Async progress |                |
| user_data | User data.     | \[allow-none\] |

------------------------------------------------------------------------

### ostree_repo_sign_commit ()

``` programlisting
gboolean
ostree_repo_sign_commit (OstreeRepo *self,
                         const gchar *commit_checksum,
                         const gchar *key_id,
                         const gchar *homedir,
                         GCancellable *cancellable,
                         GError **error);
```

Add a GPG signature to a commit.

#### Parameters

|                 |                                |                |
|-----------------|--------------------------------|----------------|
| self            | Self                           |                |
| commit_checksum | SHA256 of given commit to sign |                |
| key_id          | Use this GPG key id            |                |
| homedir         | GPG home directory, or `NULL`. | \[allow-none\] |
| cancellable     | A GCancellable                 |                |
| error           | a GError                       |                |

------------------------------------------------------------------------

### ostree_repo_append_gpg_signature ()

``` programlisting
gboolean
ostree_repo_append_gpg_signature (OstreeRepo *self,
                                  const gchar *commit_checksum,
                                  GBytes *signature_bytes,
                                  GCancellable *cancellable,
                                  GError **error);
```

Append a GPG signature to a commit.

#### Parameters

|                 |                                |     |
|-----------------|--------------------------------|-----|
| self            | Self                           |     |
| commit_checksum | SHA256 of given commit to sign |     |
| signature_bytes | Signature data                 |     |
| cancellable     | A GCancellable                 |     |
| error           | a GError                       |     |

------------------------------------------------------------------------

### ostree_repo_add_gpg_signature_summary ()

``` programlisting
gboolean
ostree_repo_add_gpg_signature_summary (OstreeRepo *self,
                                       const gchar **key_id,
                                       const gchar *homedir,
                                       GCancellable *cancellable,
                                       GError **error);
```

Add a GPG signature to a summary file.

#### Parameters

|  |  |  |
|----|----|----|
| self | Self |   |
| key_id | NULL-terminated array of GPG keys. | \[array zero-terminated=1\]\[element-type utf8\] |
| homedir | GPG home directory, or `NULL`. | \[allow-none\] |
| cancellable | A GCancellable |   |
| error | a GError |   |

------------------------------------------------------------------------

### ostree_repo_gpg_sign_data ()

``` programlisting
gboolean
ostree_repo_gpg_sign_data (OstreeRepo *self,
                           GBytes *data,
                           GBytes *old_signatures,
                           const gchar **key_id,
                           const gchar *homedir,
                           GBytes **out_signatures,
                           GCancellable *cancellable,
                           GError **error);
```

Sign the given *`data`* with the specified keys in *`key_id`* . Similar to [`ostree_repo_add_gpg_signature_summary()`](reference__ostree-OstreeRepo.md#ostree-repo-add-gpg-signature-summary "ostree_repo_add_gpg_signature_summary ()") but can be used on any data.

You can use [`ostree_repo_gpg_verify_data()`](reference__ostree-OstreeRepo.md#ostree-repo-gpg-verify-data "ostree_repo_gpg_verify_data ()") to verify the signatures.

#### Parameters

|  |  |  |
|----|----|----|
| self | Self |   |
| data | Data as a GBytes |   |
| old_signatures | Existing signatures to append to (or `NULL`). | \[nullable\] |
| key_id | NULL-terminated array of GPG keys. | \[array zero-terminated=1\]\[element-type utf8\] |
| homedir | GPG home directory, or `NULL`. | \[nullable\] |
| out_signatures | in case of success will contain signature. | \[out\] |
| cancellable | A GCancellable |   |
| error | a GError |   |

#### Returns

`TRUE` if *`data`* has been signed successfully, `FALSE` in case of error (*`error`* will contain the reason).

Since: 2020.8

------------------------------------------------------------------------

### ostree_repo_gpg_verify_data ()

``` programlisting
OstreeGpgVerifyResult *
ostree_repo_gpg_verify_data (OstreeRepo *self,
                             const gchar *remote_name,
                             GBytes *data,
                             GBytes *signatures,
                             GFile *keyringdir,
                             GFile *extra_keyring,
                             GCancellable *cancellable,
                             GError **error);
```

Verify *`signatures`* for *`data`* using GPG keys in the keyring for *`remote_name`* , and return an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult").

The *`remote_name`* parameter can be `NULL`. In that case it will do the verifications using GPG keys in the keyrings of all remotes.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repository |   |
| remote_name | Name of remote. | \[nullable\] |
| data | Data as a GBytes |   |
| signatures | Signatures as a GBytes |   |
| keyringdir | Path to directory GPG keyrings; overrides built-in default if given. | \[nullable\] |
| extra_keyring | Path to additional keyring file (not a directory). | \[nullable\] |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult"), or `NULL` on error.

\[transfer full\]

Since: 2016.6

------------------------------------------------------------------------

### ostree_repo_signature_verify_commit_data ()

``` programlisting
gboolean
ostree_repo_signature_verify_commit_data
                               (OstreeRepo *self,
                                const char *remote_name,
                                GBytes *commit_data,
                                GBytes *commit_metadata,
                                OstreeRepoVerifyFlags flags,
                                char **out_results,
                                GError **error);
```

Validate the commit data using the commit metadata which must contain at least one valid signature. If GPG and signapi are both enabled, then both must find at least one valid signature.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| remote_name | Name of remote |   |
| commit_data | Commit object data (GVariant) |   |
| commit_metadata | Commit metadata (GVariant `a{sv}`), must contain at least one valid signature |   |
| flags | Optionally disable GPG or signapi |   |
| out_results | Textual description of results. | \[optional\]\[out\]\[transfer full\] |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_verify_commit ()

``` programlisting
gboolean
ostree_repo_verify_commit (OstreeRepo *self,
                           const gchar *commit_checksum,
                           GFile *keyringdir,
                           GFile *extra_keyring,
                           GCancellable *cancellable,
                           GError **error);
```

Check for a valid GPG signature on commit named by the ASCII checksum *`commit_checksum`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Repository |   |
| commit_checksum | ASCII SHA256 checksum |   |
| keyringdir | Path to directory GPG keyrings; overrides built-in default if given. | \[allow-none\] |
| extra_keyring | Path to additional keyring file (not a directory). | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

`TRUE` if there was a GPG signature from a trusted keyring, otherwise `FALSE`

------------------------------------------------------------------------

### ostree_repo_verify_commit_ext ()

``` programlisting
OstreeGpgVerifyResult *
ostree_repo_verify_commit_ext (OstreeRepo *self,
                               const gchar *commit_checksum,
                               GFile *keyringdir,
                               GFile *extra_keyring,
                               GCancellable *cancellable,
                               GError **error);
```

Read GPG signature(s) on the commit named by the ASCII checksum *`commit_checksum`* and return detailed results.

#### Parameters

|  |  |  |
|----|----|----|
| self | Repository |   |
| commit_checksum | ASCII SHA256 checksum |   |
| keyringdir | Path to directory GPG keyrings; overrides built-in default if given. | \[allow-none\] |
| extra_keyring | Path to additional keyring file (not a directory). | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult"), or `NULL` on error.

\[transfer full\]

------------------------------------------------------------------------

### ostree_repo_verify_commit_for_remote ()

``` programlisting
OstreeGpgVerifyResult *
ostree_repo_verify_commit_for_remote (OstreeRepo *self,
                                      const gchar *commit_checksum,
                                      const gchar *remote_name,
                                      GCancellable *cancellable,
                                      GError **error);
```

Read GPG signature(s) on the commit named by the ASCII checksum *`commit_checksum`* and return detailed results, based on the keyring configured for *`remote`* .

#### Parameters

|                 |                                        |     |
|-----------------|----------------------------------------|-----|
| self            | Repository                             |     |
| commit_checksum | ASCII SHA256 checksum                  |     |
| remote_name     | OSTree remote to use for configuration |     |
| cancellable     | Cancellable                            |     |
| error           | Error                                  |     |

#### Returns

an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult"), or `NULL` on error.

\[transfer full\]

Since: 2016.14

------------------------------------------------------------------------

### ostree_repo_verify_summary ()

``` programlisting
OstreeGpgVerifyResult *
ostree_repo_verify_summary (OstreeRepo *self,
                            const char *remote_name,
                            GBytes *summary,
                            GBytes *signatures,
                            GCancellable *cancellable,
                            GError **error);
```

Verify *`signatures`* for *`summary`* data using GPG keys in the keyring for *`remote_name`* , and return an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult").

#### Parameters

|             |                                |     |
|-------------|--------------------------------|-----|
| self        | Repo                           |     |
| remote_name | Name of remote                 |     |
| summary     | Summary data as a GBytes       |     |
| signatures  | Summary signatures as a GBytes |     |
| cancellable | Cancellable                    |     |
| error       | Error                          |     |

#### Returns

an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult"), or `NULL` on error.

\[transfer full\]

------------------------------------------------------------------------

### ostree_repo_regenerate_metadata ()

``` programlisting
gboolean
ostree_repo_regenerate_metadata (OstreeRepo *self,
                                 GVariant *additional_metadata,
                                 GVariant *options,
                                 GCancellable *cancellable,
                                 GError **error);
```

Regenerate the OSTree repository metadata used by clients to describe available branches and other metadata.

The repository metadata currently consists of the `summary` file. See [`ostree_repo_regenerate_summary()`](reference__ostree-OstreeRepo.md#ostree-repo-regenerate-summary "ostree_repo_regenerate_summary ()") and [`OSTREE_SUMMARY_GVARIANT_FORMAT`](reference__ostree-Core-repository-independent-functions.md#OSTREE-SUMMARY-GVARIANT-FORMAT:CAPS "OSTREE_SUMMARY_GVARIANT_FORMAT") for additional details on its contents.

Additionally, if the `core/collection-id` key is set in the configuration, a [`OSTREE_REPO_METADATA_REF`](reference__ostree-ostree-repo-remote-finder.md#OSTREE-REPO-METADATA-REF:CAPS "OSTREE_REPO_METADATA_REF") commit will be created.

The following *`options`* are currently defined:

- `gpg-key-ids` (`as`): Array of GPG key IDs to sign the metadata with.

- `gpg-homedir` (`s`): GPG home directory.

- `sign-keys` (`av`): Array of keys to sign the metadata with. The key type is specific to the sign engine used.

- `sign-type` (`s`): Sign engine type to use. If not specified, `OSTREE_SIGN_NAME_ED25519` is used.

Locking: shared

#### Parameters

|  |  |  |
|----|----|----|
| self | Repo |   |
| additional_metadata | A GVariant `a{sv}`, or `NULL`. | \[nullable\] |
| options | A GVariant `a{sv}` with an extensible set of flags. | \[nullable\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2023.1

------------------------------------------------------------------------

### ostree_repo_regenerate_summary ()

``` programlisting
gboolean
ostree_repo_regenerate_summary (OstreeRepo *self,
                                GVariant *additional_metadata,
                                GCancellable *cancellable,
                                GError **error);
```

An OSTree repository can contain a high level "summary" file that describes the available branches and other metadata.

If the timetable for making commits and updating the summary file is fairly regular, setting the `ostree.summary.expires` key in *`additional_metadata`* will aid clients in working out when to check for updates.

It is regenerated automatically after any ref is added, removed, or updated if `core/auto-update-summary` is set.

If the `core/collection-id` key is set in the configuration, it will be included as `OSTREE_SUMMARY_COLLECTION_ID` in the summary file. Refs that have associated collection IDs will be included in the generated summary file, listed under the `OSTREE_SUMMARY_COLLECTION_MAP` key. Collection IDs and refs in `OSTREE_SUMMARY_COLLECTION_MAP` are guaranteed to be in lexicographic order.

Locking: shared (Prior to 2021.7, this was exclusive)

#### Parameters

|                     |                                      |                |
|---------------------|--------------------------------------|----------------|
| self                | Repo                                 |                |
| additional_metadata | A GVariant of type a{sv}, or `NULL`. | \[allow-none\] |
| cancellable         | Cancellable                          |                |
| error               | Error                                |                |

## Types and Values

### OstreeRepo

``` programlisting
typedef struct OstreeRepo OstreeRepo;
```

Private instance structure.

------------------------------------------------------------------------

### enum OstreeRepoMode

See the documentation of [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") for more information about the possible modes.

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_MODE_BARE | Files are stored as themselves; checkouts are hardlinks; can only be written as root |   |
| OSTREE_REPO_MODE_ARCHIVE | Files are compressed, should be owned by non-root. Can be served via HTTP. Since: 2017.12 |   |
| OSTREE_REPO_MODE_ARCHIVE_Z2 | Legacy alias for `OSTREE_REPO_MODE_ARCHIVE` |   |
| OSTREE_REPO_MODE_BARE_USER | Files are stored as themselves, except ownership; can be written by user. Hardlinks work only in user checkouts. |   |
| OSTREE_REPO_MODE_BARE_USER_ONLY | Same as BARE_USER, but all metadata is not stored, so it can only be used for user checkouts. Does not need xattrs. |   |
| OSTREE_REPO_MODE_BARE_SPLIT_XATTRS | Same as BARE_USER, but xattrs are stored separately from file content, with dedicated object types. |   |

------------------------------------------------------------------------

### enum OstreeRepoLockType

Flags controlling repository locking.

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_LOCK_SHARED | A "read only" lock; multiple readers are allowed. |   |
| OSTREE_REPO_LOCK_EXCLUSIVE | A writable lock at most one writer can be active, and zero readers. |   |

Since: 2021.3

------------------------------------------------------------------------

### OstreeRepoAutoLock

``` programlisting
typedef struct OstreeRepoAutoLock OstreeRepoAutoLock;
```

An opaque type for use with [`ostree_repo_auto_lock_push()`](reference__ostree-OstreeRepo.md#ostree-repo-auto-lock-push "ostree_repo_auto_lock_push ()").

Since: 2021.3

------------------------------------------------------------------------

### enum OstreeRepoRemoteChange

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_REMOTE_CHANGE_ADD | Add a remote |   |
| OSTREE_REPO_REMOTE_CHANGE_ADD_IF_NOT_EXISTS | Like above, but do nothing if the remote exists |   |
| OSTREE_REPO_REMOTE_CHANGE_DELETE | Delete a remote |   |
| OSTREE_REPO_REMOTE_CHANGE_DELETE_IF_EXISTS | Delete a remote, do nothing if the remote does not exist |   |
| OSTREE_REPO_REMOTE_CHANGE_REPLACE | Add or replace a remote (Since: 2019.2) |   |

------------------------------------------------------------------------

### struct OstreeRepoTransactionStats

``` programlisting
struct OstreeRepoTransactionStats {
  guint metadata_objects_total;
  guint metadata_objects_written;
  guint content_objects_total;
  guint content_objects_written;
  guint64 content_bytes_written;
  guint devino_cache_hits;

  guint padding1;
  guint64 padding2;
  guint64 padding3;
  guint64 padding4;
};
```

A list of statistics for each transaction that may be interesting for reporting purposes.

#### Members

|  |  |  |
|----|----|----|
| guint *`metadata_objects_total`*; | The total number of metadata objects in the repository after this transaction has completed. |   |
| guint *`metadata_objects_written`*; | The number of metadata objects that were written to the repository in this transaction. |   |
| guint *`content_objects_total`*; | The total number of content objects in the repository after this transaction has completed. |   |
| guint *`content_objects_written`*; | The number of content objects that were written to the repository in this transaction. |   |
| guint64 *`content_bytes_written`*; | The amount of data added to the repository, in bytes, counting only content objects. |   |
| guint *`devino_cache_hits`*; |   |   |
| guint *`padding1`*; | reserved |   |
| guint64 *`padding2`*; | reserved |   |
| guint64 *`padding3`*; | reserved |   |
| guint64 *`padding4`*; | reserved |   |

------------------------------------------------------------------------

### enum OstreeRepoResolveRevExtFlags

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_RESOLVE_REV_EXT_NONE | No flags. |   |
| OSTREE_REPO_RESOLVE_REV_EXT_LOCAL_ONLY | Exclude remote and mirrored refs. Since: 2019.2 |   |

------------------------------------------------------------------------

### enum OstreeRepoListRefsExtFlags

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_LIST_REFS_EXT_NONE | No flags. |   |
| OSTREE_REPO_LIST_REFS_EXT_ALIASES | Only list aliases. Since: 2017.10 |   |
| OSTREE_REPO_LIST_REFS_EXT_EXCLUDE_REMOTES | Exclude remote refs. Since: 2017.11 |   |
| OSTREE_REPO_LIST_REFS_EXT_EXCLUDE_MIRRORS | Exclude mirrored refs. Since: 2019.2 |   |

------------------------------------------------------------------------

### enum OstreeRepoCommitState

Flags representing the state of a commit in the local repository, as returned by [`ostree_repo_load_commit()`](reference__ostree-OstreeRepo.md#ostree-repo-load-commit "ostree_repo_load_commit ()").

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_COMMIT_STATE_NORMAL | Commit is complete. This is the default. (Since: 2017.14.) |   |
| OSTREE_REPO_COMMIT_STATE_PARTIAL | One or more objects are missing from the local copy of the commit, but metadata is present. (Since: 2015.7.) |   |
| OSTREE_REPO_COMMIT_STATE_FSCK_PARTIAL | One or more objects are missing from the local copy of the commit, due to an fsck --delete. (Since: 2019.4.) |   |

Since: 2015.7

------------------------------------------------------------------------

### enum OstreeRepoCommitFilterResult

#### Members

|                                 |                       |     |
|---------------------------------|-----------------------|-----|
| OSTREE_REPO_COMMIT_FILTER_ALLOW | Do commit this object |     |
| OSTREE_REPO_COMMIT_FILTER_SKIP  | Ignore this object    |     |

------------------------------------------------------------------------

### OstreeRepoCommitModifier

``` programlisting
typedef struct OstreeRepoCommitModifier OstreeRepoCommitModifier;
```

A structure allowing control over commits.

------------------------------------------------------------------------

### enum OstreeRepoCommitModifierFlags

Flags modifying commit behavior. In bare-user-only mode, *`OSTREE_REPO_COMMIT_MODIFIER_FLAGS_CANONICAL_PERMISSIONS`* and *`OSTREE_REPO_COMMIT_MODIFIER_FLAGS_SKIP_XATTRS`* are automatically enabled.

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_COMMIT_MODIFIER_FLAGS_NONE | No special flags |   |
| OSTREE_REPO_COMMIT_MODIFIER_FLAGS_SKIP_XATTRS | Do not process extended attributes |   |
| OSTREE_REPO_COMMIT_MODIFIER_FLAGS_GENERATE_SIZES | Generate size information. |   |
| OSTREE_REPO_COMMIT_MODIFIER_FLAGS_CANONICAL_PERMISSIONS | Canonicalize permissions. |   |
| OSTREE_REPO_COMMIT_MODIFIER_FLAGS_ERROR_ON_UNLABELED | Emit an error if configured SELinux policy does not provide a label |   |
| OSTREE_REPO_COMMIT_MODIFIER_FLAGS_CONSUME | Delete added files/directories after commit; Since: 2017.13 |   |
| OSTREE_REPO_COMMIT_MODIFIER_FLAGS_DEVINO_CANONICAL | If a devino cache hit is found, skip modifier filters (non-directories only); Since: 2017.14 |   |
| OSTREE_REPO_COMMIT_MODIFIER_FLAGS_SELINUX_LABEL_V1 | For SELinux and other systems, label /usr/etc as if it was /etc. |   |

------------------------------------------------------------------------

### enum OstreeRepoCheckoutMode

#### Members

|                                |                         |     |
|--------------------------------|-------------------------|-----|
| OSTREE_REPO_CHECKOUT_MODE_NONE | No special options      |     |
| OSTREE_REPO_CHECKOUT_MODE_USER | Ignore uid/gid of files |     |

------------------------------------------------------------------------

### enum OstreeRepoCheckoutOverwriteMode

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_CHECKOUT_OVERWRITE_NONE | No special options |   |
| OSTREE_REPO_CHECKOUT_OVERWRITE_UNION_FILES | When layering checkouts, `unlink()` and replace existing files, but do not modify existing directories (unless whiteouts are enabled, then directories are replaced) |   |
| OSTREE_REPO_CHECKOUT_OVERWRITE_ADD_FILES | Only add new files/directories |   |
| OSTREE_REPO_CHECKOUT_OVERWRITE_UNION_IDENTICAL | Like UNION_FILES, but error if files are not identical (requires hardlink checkouts) |   |

------------------------------------------------------------------------

### enum OstreeRepoListObjectsFlags

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_LIST_OBJECTS_LOOSE | List only loose (plain file) objects |   |
| OSTREE_REPO_LIST_OBJECTS_PACKED | List only packed (compacted into blobs) objects |   |
| OSTREE_REPO_LIST_OBJECTS_ALL | List all objects |   |
| OSTREE_REPO_LIST_OBJECTS_NO_PARENTS | Only list objects in this repo, not parents |   |

------------------------------------------------------------------------

### OSTREE_REPO_LIST_OBJECTS_VARIANT_TYPE

``` programlisting
#define OSTREE_REPO_LIST_OBJECTS_VARIANT_TYPE (G_VARIANT_TYPE ("(bas)")
```

b - `TRUE` if object is available "loose" as - List of pack file checksums in which this object appears

------------------------------------------------------------------------

### enum OstreeStaticDeltaGenerateOpt

Parameters controlling optimization of static deltas.

#### Members

|  |  |  |
|----|----|----|
| OSTREE_STATIC_DELTA_GENERATE_OPT_LOWLATENCY | Optimize for speed of delta creation over space |   |
| OSTREE_STATIC_DELTA_GENERATE_OPT_MAJOR | Optimize for delta size (may be very slow) |   |

------------------------------------------------------------------------

### enum OstreeRepoCommitTraverseFlags

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_COMMIT_TRAVERSE_FLAG_NONE | No special options for traverse |   |
| OSTREE_REPO_COMMIT_TRAVERSE_FLAG_COMMIT_ONLY | Traverse and retrieve only commit objects. (Since: 2022.2) |   |

------------------------------------------------------------------------

### enum OstreeRepoCommitIterResult

#### Members

|                                      |     |     |
|--------------------------------------|-----|-----|
| OSTREE_REPO_COMMIT_ITER_RESULT_ERROR |     |     |
| OSTREE_REPO_COMMIT_ITER_RESULT_END   |     |     |
| OSTREE_REPO_COMMIT_ITER_RESULT_FILE  |     |     |
| OSTREE_REPO_COMMIT_ITER_RESULT_DIR   |     |     |

------------------------------------------------------------------------

### enum OstreeRepoPruneFlags

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_PRUNE_FLAGS_NONE | No special options for pruning |   |
| OSTREE_REPO_PRUNE_FLAGS_NO_PRUNE | Don't actually delete objects |   |
| OSTREE_REPO_PRUNE_FLAGS_REFS_ONLY | Do not traverse individual commit objects, only follow refs for reachability calculations |   |
| OSTREE_REPO_PRUNE_FLAGS_COMMIT_ONLY | Only traverse commit objects. (Since 2022.2) |   |

------------------------------------------------------------------------

### enum OstreeRepoPullFlags

#### Members

|  |  |  |
|----|----|----|
| OSTREE_REPO_PULL_FLAGS_NONE | No special options for pull |   |
| OSTREE_REPO_PULL_FLAGS_MIRROR | Write out refs suitable for mirrors and fetch all refs if none requested |   |
| OSTREE_REPO_PULL_FLAGS_COMMIT_ONLY | Fetch only the commit metadata |   |
| OSTREE_REPO_PULL_FLAGS_UNTRUSTED | Do verify checksums of local (filesystem-accessible) repositories (defaults on for HTTP) |   |
| OSTREE_REPO_PULL_FLAGS_BAREUSERONLY_FILES | Since 2017.7. Reject writes of content objects with modes outside of 0775. |   |
| OSTREE_REPO_PULL_FLAGS_TRUSTED_HTTP | Don't verify checksums of objects HTTP repositories (Since: 2017.12) |   |

------------------------------------------------------------------------
