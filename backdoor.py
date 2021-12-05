from ryu.base.app_manager import AppManager
am = AppManager.get_instance()
myapp = am.applications["SimpleMPLS"]
myapp.make_lsp("H1-S1-S2-S4-H6")
myapp.make_lsp("H3-S1-S2-S4-S5-H9")
myapp.show_all_lsps()
myapp.make_lsp("H2-S1-S2-H5")
myapp.show_all_lsps()
myapp.remove_lsp("H1-S1-S2-S4-H6")
myapp.remove_lsp("H3-S1-S2-S4-S5-H9")
myapp.show_all_lsps()
myapp.remove_lsp("H2-S1-S2-H5")