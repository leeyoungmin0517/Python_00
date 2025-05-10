from TSMaster import *
import sys
blacklist = ["tkinter"] # modules such as tkinter will release GIL by itself, which is not allowed in TSMster Toolbox
for mod in blacklist:
    if sys.modules.get(mod):
        tmp_import = __import__ (mod)
        sys.modules[mod] = None

# Auto Generated Python Code, do not modify START [UI] --------------
class test(frmTSForm):
    def __init__(self):
        # set type name internally
        self.ExternalTypeName = type(self).__name__
        if hasattr(self, "on_before_ui_creation"):
            method = getattr(self, "on_before_ui_creation")
            method()
        try:
            # Form properties
            if not self.IsConfigurationLoaded:
                self.Left = 156
                self.Top = 156
                self.Caption = 'test'
                self.ClientHeight = 502
                self.ClientWidth = 786
            self.Color = clBtnFace
            self.DoubleBuffered = True
            self.Font.Charset = DEFAULT_CHARSET
            self.Font.Color = clWindowText
            self.Font.Height = -12
            self.Font.Name = 'Segoe UI'
            self.Font.Style = []
            self.KeyPreview = True
            self.Position = "poDesigned"
            self.Visible = True
            self.TextHeight = 15
            # Create control: Button1 = Button(self)
            self.Button1 = Button(self)
            self.Button1.Name = "Button1"
            self.Button1.Parent = self
            self.Button1.Left = 88
            self.Button1.Top = 104
            self.Button1.Width = 75
            self.Button1.Height = 25
            self.Button1.Cursor = crArrow
            self.Button1.CustomHint = app.ui_get_default_ballon_hint()
            self.Button1.Caption = 'Button1'
            self.Button1.Images = app.get_system_imagelist_16px()
            self.Button1.TabOrder = 0
            # Create control: Edit1 = Edit(self)
            self.Edit1 = Edit(self)
            self.Edit1.Name = "Edit1"
            self.Edit1.Parent = self
            self.Edit1.Left = 192
            self.Edit1.Top = 104
            self.Edit1.Width = 192
            self.Edit1.Height = 23
            self.Edit1.Cursor = crArrow
            self.Edit1.TabOrder = 9
            self.Edit1.Text = 'Edit1'
        finally:
            # End UI auto creation
            self.EndUIAutoCreation()
# Auto Generated Python Code, do not modify END [UI] ----------------
        # your init code starts here...
        
# Auto Generated Python Code, do not modify START [MAIN] ------------
if __name__ == "__main__":
    try:
        test().Show()
        Application.Run()
    except SystemExit:
        pass
# Auto Generated Python Code, do not modify END [MAIN] --------------
