# !/usr/bin/python
# coding:utf-8


from wx import *
import net_UI2
import net_tools

class CalFrame(net_UI2.MyFrame2):
    def __init__(self, parent):
        net_UI2.MyFrame2.__init__(self,parent)




    def Calnet(self, event):
        '''
        计算网络地址
        :param event:
        :return:
        '''

        ip = self.m_textCtrl1.GetValue()  # 获取ip
        mask_bit = str(self.m_choice2.GetCurrentSelection())   # 获取掩码位
        # print mask_bit
        host_num = net_tools.host_num(mask_bit)   #可用主机数
        self.m_textCtrl2.SetValue(str(host_num))

        net = net_tools.networkAddr(ip,mask_bit)   #网络地址
        # print net
        self.m_textCtrl4.SetValue(str(net))


        netmask = net_tools.netmask(ip, mask_bit)  #掩码
        self.m_textCtrl3.SetValue(str(netmask))

        firstAddr = net_tools.firstAvailAddr(ip, mask_bit)
        self.m_textCtrl6.SetValue(str(firstAddr))

        # lastAddr = net_tools.lastAvailAddr(ip, mask_bit)
        # self.m_textCtrl10.SetValue(str(lastAddr))

        broadcast = net_tools.broadcast(ip, mask_bit)
        self.m_textCtrl5.SetValue(str(broadcast))

        return ip,mask_bit,net,netmask,firstAddr,broadcast


    def subnet_exchange(self,event):
        '''
        子网掩码转换
        255.255.255.0————————>24
        '''
        netmask1 = self.m_textCtrl10.GetValue()

        bits_sum = net_tools.exchange_mask(netmask1)

        self.m_textCtrl11.SetValue(bits_sum)

    def bits_exchange(self, event):

        bits = self.m_textCtrl12.GetValue()
        lists = net_tools.exchange_bit(bits)
        try:
            netmask = lists[0]
            netmask_hex = lists[1]
        except Exception:
            netmask = lists[0]
            netmask_hex= lists[0]

        self.m_textCtrl14.SetValue(netmask)
        self.m_textCtrl15.SetValue(netmask_hex)

    def ip_exchange(self,event):

        ip = self.m_textCtrl7.GetValue()
        lists = net_tools.exchange_ip(ip)
        try:
            ip_str = lists[0]
            ip_hex = lists[1]
        except Exception:
            ip_str = lists[0]
            ip_hex = lists[0]
        self.m_textCtrl8.SetValue(ip_str)
        self.m_textCtrl9.SetValue(ip_hex)

    def get(self,event):
        ip = self.m_textCtrl2.GetValue()  # 获取ip
        mask_bit = self.m_textCtrl3.GetValue()  # 获取掩码位
    def get_list(self, event):

        ip, mask_bit, net, netmask, firstAddr, broadcast = self.Calnet(event)
        ip_data = '输入的ip为:{0}'.format(ip)
        mask_bit_data = '输入的掩码位:{0}'.format(str(mask_bit))
        net_data = '网络地址为:{0}'.format(str(net))
        netmask_data = '掩码：{0}'.format(str(netmask))
        firstAddr_data = '第一个可用地址：{0}'.format(str(firstAddr))
        broadcast_data = '广播地址：{0}'.format(str(broadcast))

        l = net_tools.subnet_ip(ip, mask_bit)
        try:
            with open('/home/xujn/桌面/net.txt', 'w') as f:
                f.write("网络和IP转换器\n")
                f.write(str(ip_data))
                f.write('\n')
                f.write(mask_bit_data)
                f.write('\n')
                f.write(net_data)
                f.write('\n')
                f.write(netmask_data)
                f.write('\n')
                f.write(firstAddr_data)
                f.write('\n')
                f.write(broadcast_data)
                f.write('\n')

                f.write('网络地址列表')
                f.write('\n')
                for i in l:
                    f.write(str(i))
                    f.write('\n')
                f.write("子网掩码转换器\n")

                f.close()
        except Exception:
            dlg = wx.MessageDialog(None, u"导出失败", u"错误", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                # self.Close(True)
                dlg.Destroy()
    def get_host(self,event):
        hname = net_tools.get_ip_hostname()[0]
        mac = net_tools.get_mac_address()

        ip_mac = str(hname+":"+mac)
        self.m_textCtrl151.SetValue(ip_mac)
app1 = wx.App()
frame = CalFrame(None)
frame.Show()
# 主循环
app1.MainLoop()
