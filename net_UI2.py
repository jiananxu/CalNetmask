# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"子网掩码计算器", pos=wx.DefaultPosition, size=wx.Size(826, 554),
                          style=wx.DEFAULT_FRAME_STYLE | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu2 = wx.Menu()
        self.m_menu1 = wx.Menu()
        self.m_menuItem2 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"item1", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem2)

        self.m_menu1.AppendSeparator()

        self.m_menuItem3 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"item2", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem3)

        self.m_menu2.AppendSubMenu(self.m_menu1, u"子菜单")

        self.m_menubar1.Append(self.m_menu2, u"菜单")

        self.m_menu21 = wx.Menu()
        self.m_menu22 = wx.Menu()
        self.m_menu21.AppendSubMenu(self.m_menu22, u"MyMenu")

        self.m_menubar1.Append(self.m_menu21, u"导出")

        self.SetMenuBar(self.m_menubar1)

        gSizer11 = wx.GridSizer(2, 2, 0, 0)

        gSizer12 = wx.GridSizer(1, 1, 0, 0)

        gSizer18 = wx.GridSizer(8, 4, 0, 0)

        self.m_staticText29 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)
        gSizer18.Add(self.m_staticText29, 0, wx.ALL, 5)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, u"网络和IP计算器", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        self.m_staticText30.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText30.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))

        gSizer18.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gSizer18.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.m_staticText32 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)
        gSizer18.Add(self.m_staticText32, 0, wx.ALL, 5)

        self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, u"IP/掩码位：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        gSizer18.Add(self.m_staticText33, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer18.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_staticText34 = wx.StaticText(self, wx.ID_ANY, u"      /", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        gSizer18.Add(self.m_staticText34, 0, wx.ALL, 5)

        m_choice2Choices = [u"0", u"1", u"2", u"3", u"4", u"5", u"67", u"7", u"8", u"9", u"10", u"11", u"12", u"13",
                            u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26",
                            u"27", u"29", u"30", u"31", u"32", wx.EmptyString]
        self.m_choice2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        self.m_choice2.SetSelection(14)
        gSizer18.Add(self.m_choice2, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer18.Add(self.m_button1, 0, 0, 5)

        self.m_staticText35 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gSizer18.Add(self.m_staticText35, 0, wx.ALL, 5)

        self.m_staticText36 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText36.Wrap(-1)
        gSizer18.Add(self.m_staticText36, 0, wx.ALL, 5)

        self.m_staticText37 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText37.Wrap(-1)
        gSizer18.Add(self.m_staticText37, 0, wx.ALL, 5)

        self.m_staticText38 = wx.StaticText(self, wx.ID_ANY, u"可用地址：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText38.Wrap(-1)
        gSizer18.Add(self.m_staticText38, 0, wx.ALL, 5)

        self.m_staticText58 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText58.Wrap(-1)
        gSizer18.Add(self.m_staticText58, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl2.SetForegroundColour(wx.Colour(0, 255, 0))

        gSizer18.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.m_staticText59 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText59.Wrap(-1)
        gSizer18.Add(self.m_staticText59, 0, wx.ALL, 5)

        self.m_staticText60 = wx.StaticText(self, wx.ID_ANY, u"子网掩码：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText60.Wrap(-1)
        gSizer18.Add(self.m_staticText60, 0, wx.ALL, 5)

        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        gSizer18.Add(self.m_staticText61, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl3.SetForegroundColour(wx.Colour(51, 210, 0))

        gSizer18.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_staticText62 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText62.Wrap(-1)
        gSizer18.Add(self.m_staticText62, 0, wx.ALL, 5)

        self.m_staticText63 = wx.StaticText(self, wx.ID_ANY, u"网络地址：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText63.Wrap(-1)
        gSizer18.Add(self.m_staticText63, 0, wx.ALL, 5)

        self.m_staticText64 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText64.Wrap(-1)
        gSizer18.Add(self.m_staticText64, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl4.SetForegroundColour(wx.Colour(0, 255, 24))

        gSizer18.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        self.m_staticText65 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65.Wrap(-1)
        gSizer18.Add(self.m_staticText65, 0, wx.ALL, 5)

        self.m_staticText66 = wx.StaticText(self, wx.ID_ANY, u"广播地址", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText66.Wrap(-1)
        gSizer18.Add(self.m_staticText66, 0, wx.ALL, 5)

        self.m_staticText67 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText67.Wrap(-1)
        gSizer18.Add(self.m_staticText67, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl5.SetForegroundColour(wx.Colour(8, 255, 0))

        gSizer18.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.m_staticText68 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText68.Wrap(-1)
        gSizer18.Add(self.m_staticText68, 0, wx.ALL, 5)

        self.m_staticText69 = wx.StaticText(self, wx.ID_ANY, u"第一个可用地址", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText69.Wrap(-1)
        gSizer18.Add(self.m_staticText69, 0, wx.ALL, 5)

        self.m_staticText73 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText73.Wrap(-1)
        gSizer18.Add(self.m_staticText73, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl6.SetForegroundColour(wx.Colour(0, 255, 6))

        gSizer18.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        gSizer12.Add(gSizer18, 1, wx.EXPAND, 6)

        gSizer11.Add(gSizer12, 1, wx.EXPAND, 5)

        gSizer13 = wx.GridSizer(4, 2, 0, 0)

        self.m_staticText76 = wx.StaticText(self, wx.ID_ANY, u"IP地址十进制转换二进制和十六进制", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText76.Wrap(-1)
        self.m_staticText76.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        gSizer13.Add(self.m_staticText76, 0, wx.ALL, 5)

        self.m_staticText77 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText77.Wrap(-1)
        gSizer13.Add(self.m_staticText77, 0, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer13.Add(self.m_textCtrl7, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        gSizer13.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_staticText78 = wx.StaticText(self, wx.ID_ANY, u"二进制：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText78.Wrap(-1)
        gSizer13.Add(self.m_staticText78, 0, wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer13.Add(self.m_textCtrl8, 0, wx.ALL, 5)

        self.m_staticText79 = wx.StaticText(self, wx.ID_ANY, u"十六进制：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText79.Wrap(-1)
        gSizer13.Add(self.m_staticText79, 0, wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer13.Add(self.m_textCtrl9, 0, wx.ALL, 5)

        gSizer11.Add(gSizer13, 1, wx.EXPAND, 5)

        gSizer14 = wx.GridSizer(5, 2, 0, 0)

        self.m_staticText80 = wx.StaticText(self, wx.ID_ANY, u"                子网掩码转换器", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText80.Wrap(-1)
        self.m_staticText80.SetForegroundColour(wx.Colour(0, 72, 255))

        gSizer14.Add(self.m_staticText80, 0, wx.ALL, 5)

        self.m_staticText81 = wx.StaticText(self, wx.ID_ANY, u"（对位点分十进制格式）", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)
        self.m_staticText81.SetForegroundColour(wx.Colour(0, 8, 255))

        gSizer14.Add(self.m_staticText81, 0, wx.ALL, 5)

        gSizer14.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        gSizer14.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl10.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_textCtrl10.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        gSizer14.Add(self.m_textCtrl10, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer14.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_staticText82 = wx.StaticText(self, wx.ID_ANY, u"结果：                            /", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText82.Wrap(-1)
        gSizer14.Add(self.m_staticText82, 0, wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer14.Add(self.m_textCtrl11, 0, wx.ALL, 5)

        self.m_staticText87 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText87.Wrap(-1)
        gSizer14.Add(self.m_staticText87, 0, wx.ALL, 5)

        self.m_staticText88 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText88.Wrap(-1)
        gSizer14.Add(self.m_staticText88, 0, wx.ALL, 5)

        gSizer11.Add(gSizer14, 1, wx.EXPAND, 5)

        gSizer15 = wx.GridSizer(7, 2, 0, 0)

        self.m_staticText83 = wx.StaticText(self, wx.ID_ANY, u"                  子网掩码转换器", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText83.Wrap(-1)
        self.m_staticText83.SetForegroundColour(wx.Colour(0, 22, 255))

        gSizer15.Add(self.m_staticText83, 0, wx.ALL, 5)

        self.m_staticText84 = wx.StaticText(self, wx.ID_ANY, u"（位点分十进制格式）", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText84.Wrap(-1)
        self.m_staticText84.SetForegroundColour(wx.Colour(0, 24, 255))

        gSizer15.Add(self.m_staticText84, 0, wx.ALL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer15.Add(self.m_textCtrl12, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer15.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_staticText85 = wx.StaticText(self, wx.ID_ANY, u"DEC十进制：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText85.Wrap(-1)
        gSizer15.Add(self.m_staticText85, 0, wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer15.Add(self.m_textCtrl14, 0, wx.ALL, 5)

        self.m_staticText86 = wx.StaticText(self, wx.ID_ANY, u"HEX十六进制：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText86.Wrap(-1)
        gSizer15.Add(self.m_staticText86, 0, wx.ALL, 5)

        self.m_textCtrl15 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer15.Add(self.m_textCtrl15, 0, wx.ALL, 5)

        gSizer15.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        gSizer15.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"查看本机主机名和mac地址", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer15.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_textCtrl151 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer15.Add(self.m_textCtrl151, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"导出到文件", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer15.Add(self.m_button7, 0, wx.ALL, 5)

        gSizer11.Add(gSizer15, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer11)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.Calnet)
        self.m_button2.Bind(wx.EVT_BUTTON, self.ip_exchange)
        self.m_button3.Bind(wx.EVT_BUTTON, self.subnet_exchange)
        self.m_button4.Bind(wx.EVT_BUTTON, self.bits_exchange)
        self.m_button6.Bind(wx.EVT_BUTTON, self.get_host)
        self.m_button7.Bind(wx.EVT_BUTTON, self.get_list)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Calnet(self, event):
        event.Skip()

    def ip_exchange(self, event):
        event.Skip()

    def subnet_exchange(self, event):
        event.Skip()

    def bits_exchange(self, event):
        event.Skip()

    def get_host(self, event):
        event.Skip()

    def get_list(self, event):
        event.Skip()


