import sys
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, cairo

class ZeroPaint(Gtk.Window):
    def __init__(self):
        super().__init__(title="Zero Paint - Ultimate Studio")
        self.set_default_size(1400, 900)
        
        self.header = Gtk.HeaderBar()
        self.header.set_show_close_button(True)
        self.header.props.title = ""
        self.header.get_style_context().add_class("hidden-header")
        self.set_titlebar(self.header)
        
        self.setup_css()
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(main_box)
        
        # ================= LEFT TOOLBAR (Tools) =================
        self.toolbar_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.toolbar_left.set_size_request(60, -1)
        self.toolbar_left.get_style_context().add_class("toolbar-side")
        main_box.pack_start(self.toolbar_left, False, False, 0)
        
        tools = ["🖌️", "✏️", "🧽", "🪣", "✂️", "🪄", "T", "✋", "🔍"]
        for t in tools:
            btn = Gtk.Button(label=t)
            btn.get_style_context().add_class("tool-btn")
            self.toolbar_left.pack_start(btn, False, False, 0)
            
        color_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        color_box.get_style_context().add_class("color-picker")
        color_box.set_size_request(40, 40)
        color_box.set_margin_top(20)
        self.toolbar_left.pack_start(color_box, False, False, 0)
        
        # ================= CANVAS =================
        self.workspace = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.workspace.get_style_context().add_class("workspace")
        main_box.pack_start(self.workspace, True, True, 0)
        
        top_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        top_bar.get_style_context().add_class("top-bar")
        self.workspace.pack_start(top_bar, False, False, 0)
        
        l_doc = Gtk.Label(label="Untitled-1 @ 100% (RGB/8)")
        l_doc.get_style_context().add_class("doc-title")
        l_doc.set_margin_start(20)
        top_bar.pack_start(l_doc, False, False, 0)
        
        canvas_align = Gtk.Alignment.new(0.5, 0.5, 0, 0)
        self.canvas = Gtk.DrawingArea()
        self.canvas.set_size_request(800, 600)
        self.canvas.get_style_context().add_class("canvas-area")
        self.canvas.connect("draw", self.on_draw)
        canvas_align.add(self.canvas)
        
        scroll = Gtk.ScrolledWindow()
        scroll.add(canvas_align)
        self.workspace.pack_start(scroll, True, True, 0)
        
        # ================= RIGHT PANEL (Layers) =================
        self.panel_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.panel_right.set_size_request(280, -1)
        self.panel_right.get_style_context().add_class("panel-right")
        main_box.pack_start(self.panel_right, False, False, 0)
        
        l_layers = Gtk.Label(label="LAYERS")
        l_layers.get_style_context().add_class("section-label")
        l_layers.set_halign(Gtk.Align.START)
        l_layers.set_margin_start(20)
        l_layers.set_margin_top(20)
        l_layers.set_margin_bottom(10)
        self.panel_right.pack_start(l_layers, False, False, 0)
        
        layers = ["Layer 3", "Layer 2", "Background"]
        for i, l in enumerate(layers):
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            box.get_style_context().add_class("layer-row")
            if i == 0:
                box.get_style_context().add_class("layer-selected")
            
            eye = Gtk.Label(label="👁️")
            eye.set_margin_start(10)
            eye.set_margin_end(10)
            
            lbl = Gtk.Label(label=l)
            lbl.get_style_context().add_class("layer-name")
            
            box.pack_start(eye, False, False, 0)
            box.pack_start(lbl, False, False, 0)
            self.panel_right.pack_start(box, False, False, 2)
            
    def on_draw(self, widget, cr):
        cr.set_source_rgb(1, 1, 1)
        cr.paint()
        
        # Draw something abstract
        cr.set_source_rgba(0.9, 0.2, 0.5, 0.8)
        cr.arc(400, 300, 150, 0, 2*3.14)
        cr.fill()
        
        cr.set_source_rgba(0.2, 0.5, 0.9, 0.6)
        cr.arc(300, 200, 100, 0, 2*3.14)
        cr.fill()

    def setup_css(self):
        css = b'''
            window { background-color: #1e1e1e; }
            .hidden-header { background: #1e1e1e; min-height: 0px; padding: 0px; border: none; box-shadow: none; }
            .toolbar-side { background-color: #252526; border-right: 1px solid #333333; padding-top: 10px; }
            .tool-btn { background: transparent; color: #CCCCCC; border: none; font-size: 20px; padding: 12px; transition: all 0.2s; border-radius: 8px; margin: 2px 5px; }
            .tool-btn:hover { background: rgba(255,255,255,0.1); color: #FFFFFF; }
            .color-picker { background-color: #FF0066; border-radius: 20px; border: 3px solid #FFFFFF; margin-left: 10px; margin-right: 10px; }
            .workspace { background-color: #111111; }
            .top-bar { background-color: #2d2d2d; padding: 10px; border-bottom: 1px solid #000000; }
            .doc-title { color: #cccccc; font-size: 13px; font-weight: bold; }
            .canvas-area { box-shadow: 0 0 20px rgba(0,0,0,0.8); }
            .panel-right { background-color: #252526; border-left: 1px solid #333333; }
            .section-label { color: #888888; font-size: 11px; font-weight: 900; letter-spacing: 1px; }
            .layer-row { background: transparent; padding: 8px 0px; margin: 0 10px; border-radius: 5px; }
            .layer-row:hover { background: rgba(255,255,255,0.05); }
            .layer-selected { background: #094771; }
            .layer-selected:hover { background: #094771; }
            .layer-name { color: #FFFFFF; font-size: 13px; }
        '''
        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == "__main__":
    win = ZeroPaint()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
