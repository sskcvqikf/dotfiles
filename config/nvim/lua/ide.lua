local bufferlist = require("ide.components.bufferlist")
local explorer = require("ide.components.explorer")
local outline = require("ide.components.outline")
local callhierarchy = require("ide.components.callhierarchy")
local timeline = require("ide.components.timeline")
local terminal = require("ide.components.terminal")
local terminalbrowser = require("ide.components.terminal.terminalbrowser")
local changes = require("ide.components.changes")
local commits = require("ide.components.commits")
local branches = require("ide.components.branches")
local bookmarks = require("ide.components.bookmarks")

StartIde = function()
	require("ide").setup({
		icon_set = "default",
		log_level = "info",
		components = {
			global_keymaps = {
				-- example, change all Component's hide keymap to "h"
				-- hide = h
			},
			-- example, prefer "x" for hide only for Explorer component.
			-- Explorer = {
			--     keymaps = {
			--         hide = "x",
			--     }
			-- }
		},
		panels = {
			left = "explorer",
			right = "git",
		},
		panel_groups = {
			explorer = {
				outline.Name,
				bufferlist.Name,
				explorer.Name,
				bookmarks.Name,
				callhierarchy.Name,
				terminalbrowser.Name,
			},
			terminal = { terminal.Name },
			git = { changes.Name, commits.Name, timeline.Name, branches.Name },
		},
		workspaces = {
			auto_open = "left",
		},
		panel_sizes = {
			left = 30,
			right = 30,
			bottom = 15,
		},
	})
end

vim.keymap.set("n", "<leader>i", StartIde, { desc = "Start IDE mode" })


