import wx
from Lipsum import GenerateLipsum

class NewLipsum(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(NewLipsum, self).__init__(*args, **kwargs)

        self.panel = wx.Panel(self, -1)

        # slider mechanism and word counter
        help_text = "Drag the slider to change the length of the Lipsum, then hit the 'Generate' button."
        self.instructions = wx.StaticText(self.panel, -1,
                                          help_text)
        self.slider = wx.Slider(self.panel, -1, minValue=1,
                                maxValue=1000,
                                style=wx.SL_HORIZONTAL | wx.SL_VALUE_LABEL)
        self.generate = wx.Button(self.panel, -1, "Generate!")
        self.textbox = wx.TextCtrl(self.panel, -1,
                                   style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.generate.Bind(wx.EVT_BUTTON, self.OnGenerate)

        self.gridsizer = wx.GridBagSizer(8, 5)
        self.gridsizer.Add(self.instructions, (0,0), (1,5))
        self.gridsizer.Add(self.slider, (1,0), (1,5), flag=wx.EXPAND)
        self.gridsizer.Add(self.generate, (1,5), (1,1))
        self.gridsizer.Add(self.textbox, (2,0), (15,6), flag=wx.EXPAND)

        self.panel.SetSizer(self.gridsizer)
        self.gridsizer.Fit(self)

    def OnGenerate(self, event):
        """
        Event handler for the 'generate' button in the app.
        :param event: event provided by wxpython framework as part of event handling mechanisms
        :return: nothing
        """
        length = self.slider.GetValue()
        # quick fix until I can figure out how to get the slider
        # to default to 1 as minValue without the labels
        # showing 0.
        if length == 0:
            length == 1
        self.textbox.SetValue(GenerateLipsum(length))

class NewApp(wx.App):
    def OnInit(self):
        myframe = NewLipsum(None, -1, "Lipsum Generator")
        myframe.Show(True)
        return True

if __name__ == "__main__":
    app = NewApp(0)
    app.MainLoop()