# Introduction

[Lua](https://www.lua.org/) is a powerful, efficient, lightweight, embeddable scripting language.

WirePlumber uses [Lua version 5.4](https://www.lua.org/versions.html) to implement its engine. For older systems, Lua 5.3 is also supported.

Scripts can be ran with the `wpexec` tool.

Example scripts can be found in the tests/examples directory of the wireplumber source tree.

## Lua Reference

If you are not familiar with the Lua language and its API, please refer to the [Lua 5.4 Reference Manual](https://www.lua.org/manual/5.4/manual.html)

## Sandbox

WirePlumber's scripting engine sandboxes the lua scripts to a safe environment. In this environment, the following rules apply:

> - Scripts are isolated from one another; global variables in one script are not visible from another, even though they are actually executed in the same `lua_State`
>
> - Tables that hold API methods are not writable. While this may sound strange, standard Lua allows you to change standard API, for instance `string.format = rogue_format` is valid outside the sandbox. WirePlumber does not allow that.
>
> - The standard Lua API is limited to a subset of safe functions. For instance, functions that interact with the file system (io.\*) and the process's state (ex.: os.exit) are **not** allowed.
>
>   Here is a full list of Lua functions (and API tables) that are exposed:

``` lua
-- WirePlumber
--
-- Copyright © 2020 Collabora Ltd.
--    @author George Kiagiadakis <george.kiagiadakis@collabora.com>
--
-- Based on https://github.com/kikito/sandbox.lua
-- Copyright © 2013 Enrique García Cota
--
-- SPDX-License-Identifier: MIT

local SANDBOX_CONFIG = ...
local SANDBOX_ENV = {}

function create_sandbox_env()
  local function populate_env(id)
    local module, method = id:match('([^%.]+)%.([^%.]+)')
    if module then
      SANDBOX_ENV[module]         = SANDBOX_ENV[module] or {}
      SANDBOX_ENV[module][method] = _G[module][method]
    else
      SANDBOX_ENV[id] = _G[id]
    end
  end

  if not SANDBOX_ENV._VERSION then
    -- List of exported functions and packages
    ([[ _VERSION assert error ipairs   next pairs  tonumber
        pcall    select print tostring type xpcall require
        table    string math  package  utf8 debug  coroutine
        os.clock  os.difftime os.time  os.date     os.getenv
        setmetatable getmetatable
    ]]):gsub('%S+', populate_env)

    -- Additionally export everything in SANDBOX_EXPORT
    if type(SANDBOX_EXPORT) == "table" then
      for k, v in pairs(SANDBOX_EXPORT) do
        SANDBOX_ENV[k] = v
      end
    end

    -- Additionally protect packages from malicious scripts trying to override methods
    for k, v in pairs(SANDBOX_ENV) do
      if type(v) == "table" then
        SANDBOX_ENV[k] = setmetatable({}, {
          __index = v,
          __call = function(t, ...)
            return t["__new"](...)
          end,
          __newindex = function(_, attr_name, _)
            error('Can not modify ' .. k .. '.' .. attr_name .. '. Protected by the sandbox.')
          end
        })
      end
    end
  end

  -- chunk's environment will be an empty table with __index
  -- to access our SANDBOX_ENV (without being able to write it)
  return setmetatable({}, {
    __index = SANDBOX_ENV,
  })
end

if SANDBOX_CONFIG["isolate_env"] then
  -- in isolate_env mode, use a separate environment for each loaded chunk and
  -- store all of them in a global table so that they are not garbage collected
  SANDBOX_ENV_LIST = {}

  function sandbox(chunk, ...)
    local env = create_sandbox_env()
    -- store the chunk's environment so that it is not garbage collected
    table.insert(SANDBOX_ENV_LIST, env)
    -- set it as the chunk's 1st upvalue (__ENV)
    debug.setupvalue(chunk, 1, env)
    -- execute the chunk
    return chunk(...)
  end
else
  -- in common_env mode, use the same environment for all loaded chunks
  -- chunk's environment will be an empty table with __index
  -- to access our SANDBOX_ENV (without being able to write it)
  SANDBOX_COMMON_ENV = create_sandbox_env()

  function sandbox(chunk, ...)
    -- set it as the chunk's 1st upvalue (__ENV)
    debug.setupvalue(chunk, 1, SANDBOX_COMMON_ENV)
    -- execute the chunk
    return chunk(...)
  end
end
```
