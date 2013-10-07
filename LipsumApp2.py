import wx
import Lipsum
import os
                
class MainFrame(wx.Frame):
        # 3 buttons at the top, text control at the bottom.
        # vertical master sizer
        # horizontal sizer w/3 buttons
        # horizontal sizer with text control
        BUTTON_0 = wx.NewId()
        BUTTON_1 = wx.NewId()
        BUTTON_2 = wx.NewId()
        BUTTON_3 = wx.NewId()
        BUTTON_4 = wx.NewId()
        ABOUT_ONE = wx.NewId()

        # I must experiment with this later:
        # IDs = [wx.NewId() for x in range(0,1000)]
        # ...
        # wx.Button(parent, ID.pop(), "BUTTON!!!")
        def UpdateSelfFo(self, string):
                self.fo = string
                self.file_txt.SetValue(string)

        def StandardMessageDialog(self, text, title):
                msg = wx.MessageDialog(self, text, title, style=wx.OK | wx.ICON_INFORMATION)
                msg.ShowModal()
                msg.Destroy()
        ########### EVENT HANDLERS
        
        def SelectFileDialog(self, event):
                dialog = wx.FileDialog(self, message="Choose a file", defaultDir=os.getcwd(),
                                       defaultFile="", style=wx.OPEN | wx.CHANGE_DIR)
                if dialog.ShowModal() == wx.ID_OK:
                        self.UpdateSelfFo(dialog.GetPath())
                        self.file_txt.SetValue(dialog.GetPath())
                dialog.Destroy()

        # There's gotta be a way to group these 3 into one function while working within the
        # constraints set by the wxPython framework.
        def GenerateSmall(self, event):
                if self.fo == None:
                        self.StandardMessageDialog("You need to select a text file before you begin!",
                                                   "Select a text file!")
                else:
                        lipsum = Lipsum.GenerateLipsum(self.fo, clean=True)
                        self.txt.Clear()
                        self.txt.SetValue(lipsum)

        def GenerateMedium(self, event):
                if self.fo == None:
                        self.StandardMessageDialog("You need to select a text file before you begin!",
                                                   "Select a text file!")
                else:
                        lipsum = Lipsum.GenerateLipsum(self.fo, max_words=500, clean=True)
                        self.txt.Clear()
                        self.txt.SetValue(lipsum)

        def GenerateLarge(self, event):
                if self.fo == None:
                        self.StandardMessageDialog("You need to select a text file before you begin!",
                                                   "Select a text file!")
                else:
                        lipsum = Lipsum.GenerateLipsum(self.fo, max_words=750, clean=True)
                        self.txt.Clear()
                        self.txt.SetValue(lipsum)

        def DisplayInstructions(self, event):
                instructions = ("This program generates a \"Lipsum\", a block of dummy text used for " +
                                "testing web page and print layouts. To use this program, first click " +
                                "\"Select File\" and then select any _text_ file. "
                                " Alternatively you can select from one of the supplied text files " +
                                " by clicking on the drop box. " + "Then select the desired " +
                                "length by clicking on one of the three buttons marked \"250 Words\", \"500 words\" "+
                                "or \"750 words\". Highlight the text, copy and paste and you're done!")
                self.txt.SetValue(instructions)

        def SelectFromChoice(self, event):
                self.UpdateSelfFo(os.getcwd() + "\\" + event.GetString() + ".txt")

        ########### EVENT HANDLERS
        def __init__(self, parent, id, title):
                initial_list = ["Raven", "Lorem Ipsum", "The City in the Sea", "Tamerlane"]
                # I love list comprehensions.
                file_list = [os.getcwd() + "\\" + initial_list[x] + ".txt" for x in range(0, len(initial_list)-1)]
                # This is the file object, the file that we will generate the lipsum from.
                self.fo = None
                
                wx.Frame.__init__(self, parent, id, title, pos=wx.DefaultPosition, size=wx.Size(640, 480))
                
                # Buttons
                panel = wx.Panel(self, -1)
                # The first row of buttons/
                select_file = wx.Button(panel, self.BUTTON_0, "Select File")
                select_file.Bind(wx.EVT_BUTTON, self.SelectFileDialog)
                button1 = wx.Button(panel, self.BUTTON_1, "250 Words")
                button1.Bind(wx.EVT_BUTTON, self.GenerateSmall)
                button2 = wx.Button(panel, self.BUTTON_2, "500 Words")
                button2.Bind(wx.EVT_BUTTON, self.GenerateMedium)
                button3 = wx.Button(panel, self.BUTTON_3, "750 Words")
                button3.Bind(wx.EVT_BUTTON, self.GenerateLarge)
                button4 = wx.Button(panel, self.BUTTON_4, "Help")
                button4.Bind(wx.EVT_BUTTON, self.DisplayInstructions)
                # The text box that displays the results.
                self.txt = wx.TextCtrl(panel, -1, "", style=wx.TE_MULTILINE | wx.TE_READONLY)

                # A list of built-in selections, so you don't have to provide your own.
                choice_desc = wx.StaticText(panel, -1, "Or select from built-in: ")
                self.choice = wx.Choice(panel, -1, choices=initial_list)
                self.choice.Bind(wx.EVT_CHOICE, self.SelectFromChoice)

                # The row that displays the file selected.
                static_txt = wx.StaticText(panel, -1, "File selected: ")
                self.file_txt = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY)

                # Now to re-do this with gridsizers instead.
                # 4 rows, 4 columns, 2 pixel gap horizontally and vertically.
                grid_master = wx.BoxSizer(wx.VERTICAL)

                # These buttons need to expand to fill their space, and then
                # expand when the windows are resized.
                # These are the buttons on the top row..
                grid = wx.BoxSizer(wx.HORIZONTAL)
                grid.Add(select_file, 1, wx.ALIGN_TOP)
                grid.Add(button1, 1, wx.ALIGN_TOP)
                grid.Add(button2, 1, wx.ALIGN_TOP)
                grid.Add(button3, 1, wx.ALIGN_TOP)
                grid.Add(button4, 1, wx.ALIGN_TOP)

                # This is the box that displays the name of the file that is currently selected.
                box1 = wx.BoxSizer(wx.HORIZONTAL)
                box1.Add(static_txt, 0, wx.ALIGN_CENTER | wx.RIGHT | wx.LEFT, border=3)
                box1.Add(self.file_txt, 1, wx.ALIGN_RIGHT)
                box1.Add(choice_desc, 0, wx.ALIGN_CENTER | wx.RIGHT | wx.LEFT, border=3)
                box1.Add(self.choice, 0, wx.ALIGN_RIGHT)

                # This is the selection box, provides a list of built-in files from which to generate
                # a lipsum from.
                #box2 = wx.BoxSizer(wx.HORIZONTAL)
                #box2.Add(choice_desc, 0, wx.ALIGN_CENTER)
                #box2.Add(self.choice, 0, wx.ALIGN_RIGHT)
                
                # This is the text control that displays the lipsum.
                grid2 = wx.BoxSizer(wx.HORIZONTAL)
                grid2.Add(self.txt, 1, wx.EXPAND)

                # FINALLY! I GOT IT WORKING!!
                # The second argument (proportion?) needs to be 0 for the top row of buttons
                # and 1 for the bottom row. This will cause the bottom row to expand to fill
                # all the space, while keeping the top row reasonably sized. >_<
                grid_master.Add(grid, 0, wx.EXPAND | wx.ALL, border=2)
                grid_master.Add(box1, 0, wx.EXPAND | wx.ALL, border=2)
                #grid_master.Add(box2, 0, wx.EXPAND | wx.ALL, border=2)
                grid_master.Add(grid2, 1, wx.EXPAND | wx.ALL, border=2)

                panel.SetSizer(grid_master)
                self.Centre()
                
class MyApp(wx.App):
        def OnInit(self):
                frame = MainFrame(None, -1, "Lipsum App v2")
                frame.Show(True)
                return True

if __name__ == "__main__":
        app = MyApp(0)
        app.MainLoop()
        
