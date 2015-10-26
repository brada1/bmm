import wx, sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
from database import Database
from downloader import Downloader
from installer import Installer

global db
db = Database.build()
    
class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)


class BMMgui(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500, 500))

        panel = wx.Panel(self, -1)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        leftPanel = wx.Panel(panel, -1)
        rightPanel = wx.Panel(panel, -1)

        self.log = wx.TextCtrl(rightPanel, -1, style=wx.TE_MULTILINE, size=(300,100))
        self.log.Enable(False)
        self.log.AppendText('connection available, starting in ' + db[1] + ' mode\n')
        self.list = CheckListCtrl(rightPanel)
        self.list.InsertColumn(0, 'ID', width=40)
        self.list.InsertColumn(1, 'Category')
        self.list.InsertColumn(2, 'Name', width=120)
        self.list.InsertColumn(3, 'Version')

        for i in db[0]:
            
            index = self.list.InsertItem(sys.maxsize, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])
            self.list.SetItem(index, 3, i[3])

        num = self.list.GetItemCount()
        for i in range(len(db[0])):
            if len(db[0][i]) == 6:
                self.list.CheckItem(i)

        vbox2 = wx.BoxSizer(wx.VERTICAL)

        sel = wx.Button(leftPanel, -1, 'Select All', size=(100, -1))
        des = wx.Button(leftPanel, -1, 'Deselect All', size=(100, -1))
        apply = wx.Button(leftPanel, -1, 'Apply', size=(100, -1))


        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id=sel.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDeselectAll, id=des.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnApply, id=apply.GetId())

        vbox2.Add(sel, 0, wx.TOP, 5)
        vbox2.Add(des)
        vbox2.Add(apply)

        leftPanel.SetSizer(vbox2)

        vbox.Add(self.list, 1, wx.EXPAND | wx.TOP, 3)
        vbox.Add((-1, 10))
        vbox.Add(self.log, 0.5, wx.EXPAND)
        vbox.Add((-1, 10))

        rightPanel.SetSizer(vbox)

        hbox.Add(leftPanel, 0, wx.EXPAND | wx.RIGHT, 5)
        hbox.Add(rightPanel, 1, wx.EXPAND)
        hbox.Add((3, -1))

        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)


    def OnSelectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i)

    def OnDeselectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i, False)

    def OnApply(self, event):
        self.log.AppendText('please wait...\n')
        for i in range(len(db[0])):
            if self.list.IsChecked(i):
                if len(db[0][i]) == 6:
                    pass
                else:
                    if len(db[0][i]) == 5:
                        pass
                    else:
                        self.log.AppendText('downloading ' + str(db[0][i]) + '...\n')
                        try:
                            Downloader.dl(db[0][i])
                        except:
                            self.log.AppendText('failed\n')
                            
                    self.log.AppendText('installing ' + str(db[0][i]) + '...\n')
                    try:
                        Installer.install(db[0][i])
                    except:
                        self.log.AppendText('failed\n')
                        
            else:
                if len(db[0][i]) == 6:
                    self.log.AppendText('uninstalling ' + str(db[0][i]) + '...\n')
                    try:
                        Installer.uninstall(db[0][i])
                    except:
                        self.log.AppendText('failed\n')
                        
        self.log.AppendText('refreshing database...\n')
        
        global db
        db = Database.build()

        self.log.AppendText('all done\n')



app = wx.App()
BMMgui(None, -1, 'Besiege Mod Manager v0.3')
app.MainLoop()
