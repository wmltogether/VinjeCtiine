# -*- coding: utf-8 -*-
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from System import Action
from System.Windows.Threading import DispatcherExtensions, Dispatcher

global currentLocale
global zhLocale

currentLocale = System.Globalization.CultureInfo.InstalledUICulture.Name
zhLocale = "zh-CN"

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        
    
    def InitializeComponent(self):
        self._label6 = System.Windows.Forms.Label()
        self._richTextBoxCurrentVC = System.Windows.Forms.RichTextBox()
        self._tabControl1 = System.Windows.Forms.TabControl()
        self._tabPage1 = System.Windows.Forms.TabPage()
        self._tabPage2 = System.Windows.Forms.TabPage()
        self._buttonSelectROMPath = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._textBoxSelectROMPath = System.Windows.Forms.TextBox()
        self._buttonStartInject = System.Windows.Forms.Button()
        self._buttonSelectDestRPXPath = System.Windows.Forms.Button()
        self._buttonSelectELFPath = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._buttonSelectRPXPath = System.Windows.Forms.Button()
        self._textBoxDestRPXPath = System.Windows.Forms.TextBox()
        self._textBoxELFPath = System.Windows.Forms.TextBox()
        self._textBoxRPXPath = System.Windows.Forms.TextBox()
        self._tabPage3 = System.Windows.Forms.TabPage()
        self._tabPage4 = System.Windows.Forms.TabPage()
        self._label7 = System.Windows.Forms.Label()
        self._textBoxTitleID = System.Windows.Forms.TextBox()
        self._richTextBox1 = System.Windows.Forms.RichTextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._tabControl1.SuspendLayout()
        self._tabPage1.SuspendLayout()
        self._tabPage2.SuspendLayout()
        self._tabPage3.SuspendLayout()
        self._tabPage4.SuspendLayout()
        self.SuspendLayout()
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(12, 316)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(390, 23)
        self._label6.TabIndex = 12
        self._label6.Text = "当前 VC 容器信息"
        if currentLocale != zhLocale:
            self._label6.Text = "current VC Information"
        # 
        # richTextBoxCurrentVC
        # 
        self._richTextBoxCurrentVC.Location = System.Drawing.Point(13, 351)
        self._richTextBoxCurrentVC.Name = "richTextBoxCurrentVC"
        self._richTextBoxCurrentVC.ReadOnly = True
        self._richTextBoxCurrentVC.Size = System.Drawing.Size(390, 91)
        self._richTextBoxCurrentVC.TabIndex = 13
        self._richTextBoxCurrentVC.Text = ""
        # 
        # tabControl1
        # 
        self._tabControl1.Controls.Add(self._tabPage1)
        self._tabControl1.Controls.Add(self._tabPage2)
        self._tabControl1.Controls.Add(self._tabPage3)
        self._tabControl1.Controls.Add(self._tabPage4)
        self._tabControl1.Location = System.Drawing.Point(12, 12)
        self._tabControl1.Name = "tabControl1"
        self._tabControl1.SelectedIndex = 0
        self._tabControl1.Size = System.Drawing.Size(501, 288)
        self._tabControl1.TabIndex = 18
        # 
        # tabPage1
        # 
        self._tabPage1.Controls.Add(self._textBoxTitleID)
        self._tabPage1.Controls.Add(self._label7)
        self._tabPage1.Controls.Add(self._buttonSelectROMPath)
        self._tabPage1.Controls.Add(self._label5)
        self._tabPage1.Controls.Add(self._textBoxSelectROMPath)
        self._tabPage1.Controls.Add(self._buttonStartInject)
        self._tabPage1.Controls.Add(self._buttonSelectDestRPXPath)
        self._tabPage1.Controls.Add(self._buttonSelectELFPath)
        self._tabPage1.Controls.Add(self._label3)
        self._tabPage1.Controls.Add(self._label2)
        self._tabPage1.Controls.Add(self._label1)
        self._tabPage1.Controls.Add(self._buttonSelectRPXPath)
        self._tabPage1.Controls.Add(self._textBoxDestRPXPath)
        self._tabPage1.Controls.Add(self._textBoxELFPath)
        self._tabPage1.Controls.Add(self._textBoxRPXPath)
        self._tabPage1.Location = System.Drawing.Point(4, 22)
        self._tabPage1.Name = "tabPage1"
        self._tabPage1.Padding = System.Windows.Forms.Padding(3)
        self._tabPage1.Size = System.Drawing.Size(493, 262)
        self._tabPage1.TabIndex = 0
        self._tabPage1.Text = "NES / SNES"
        self._tabPage1.UseVisualStyleBackColor = True
        # 
        # tabPage2
        # 
        self._tabPage2.Controls.Add(self._label4)
        self._tabPage2.Location = System.Drawing.Point(4, 22)
        self._tabPage2.Name = "tabPage2"
        self._tabPage2.Padding = System.Windows.Forms.Padding(3)
        self._tabPage2.Size = System.Drawing.Size(493, 262)
        self._tabPage2.TabIndex = 1
        self._tabPage2.Text = "GBA"
        self._tabPage2.UseVisualStyleBackColor = True
        # 
        # buttonSelectROMPath
        # 
        self._buttonSelectROMPath.Location = System.Drawing.Point(422, 170)
        self._buttonSelectROMPath.Name = "buttonSelectROMPath"
        self._buttonSelectROMPath.Size = System.Drawing.Size(27, 23)
        self._buttonSelectROMPath.TabIndex = 32
        self._buttonSelectROMPath.Text = "..."
        self._buttonSelectROMPath.UseVisualStyleBackColor = True
        self._buttonSelectROMPath.Click += self.ButtonSelectROMPathClick
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(25, 151)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(390, 16)
        self._label5.TabIndex = 31
        self._label5.Text = "ROM Path:"
        # 
        # textBoxSelectROMPath
        # 
        self._textBoxSelectROMPath.Location = System.Drawing.Point(25, 170)
        self._textBoxSelectROMPath.Name = "textBoxSelectROMPath"
        self._textBoxSelectROMPath.Size = System.Drawing.Size(390, 21)
        self._textBoxSelectROMPath.TabIndex = 30
        # 
        # buttonStartInject
        # 
        self._buttonStartInject.Location = System.Drawing.Point(330, 201)
        self._buttonStartInject.Name = "buttonStartInject"
        self._buttonStartInject.Size = System.Drawing.Size(119, 23)
        self._buttonStartInject.TabIndex = 29
        self._buttonStartInject.Text = "Let's Inject Rom!"
        self._buttonStartInject.UseVisualStyleBackColor = True
        self._buttonStartInject.Click += self.ButtonStartInjectClick
        # 
        # buttonSelectDestRPXPath
        # 
        self._buttonSelectDestRPXPath.Location = System.Drawing.Point(422, 123)
        self._buttonSelectDestRPXPath.Name = "buttonSelectDestRPXPath"
        self._buttonSelectDestRPXPath.Size = System.Drawing.Size(27, 23)
        self._buttonSelectDestRPXPath.TabIndex = 26
        self._buttonSelectDestRPXPath.Text = "..."
        self._buttonSelectDestRPXPath.UseVisualStyleBackColor = True
        self._buttonSelectDestRPXPath.Click += self.ButtonSelectDestRPXPathClick
        # 
        # buttonSelectELFPath
        # 
        self._buttonSelectELFPath.Location = System.Drawing.Point(422, 77)
        self._buttonSelectELFPath.Name = "buttonSelectELFPath"
        self._buttonSelectELFPath.Size = System.Drawing.Size(27, 23)
        self._buttonSelectELFPath.TabIndex = 25
        self._buttonSelectELFPath.Text = "..."
        self._buttonSelectELFPath.UseVisualStyleBackColor = True
        self._buttonSelectELFPath.Click += self.ButtonSelectELFPathClick
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(25, 105)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(390, 15)
        self._label3.TabIndex = 24
        self._label3.Text = "选择目标RPX:"
        if currentLocale != zhLocale:
            self._label3.Text = "Select Dest RPX:"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(24, 58)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(391, 16)
        self._label2.TabIndex = 23
        self._label2.Text = "选择ELF 路径:"
        if currentLocale != zhLocale:
            self._label2.Text = "Select ELF Path:"
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(24, 11)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(391, 14)
        self._label1.TabIndex = 22
        self._label1.Text = "选择RPX 路径:"
        if currentLocale != zhLocale:
            self._label1.Text = "Select RPX Path:"
        # 
        # buttonSelectRPXPath
        # 
        self._buttonSelectRPXPath.Location = System.Drawing.Point(422, 31)
        self._buttonSelectRPXPath.Name = "buttonSelectRPXPath"
        self._buttonSelectRPXPath.Size = System.Drawing.Size(27, 23)
        self._buttonSelectRPXPath.TabIndex = 21
        self._buttonSelectRPXPath.Text = "..."
        self._buttonSelectRPXPath.UseVisualStyleBackColor = True
        self._buttonSelectRPXPath.Click += self.ButtonSelectRPXPathClick
        # 
        # textBoxDestRPXPath
        # 
        self._textBoxDestRPXPath.Location = System.Drawing.Point(24, 123)
        self._textBoxDestRPXPath.Name = "textBoxDestRPXPath"
        self._textBoxDestRPXPath.Size = System.Drawing.Size(391, 21)
        self._textBoxDestRPXPath.TabIndex = 20
        # 
        # textBoxELFPath
        # 
        self._textBoxELFPath.Location = System.Drawing.Point(24, 77)
        self._textBoxELFPath.Name = "textBoxELFPath"
        self._textBoxELFPath.Size = System.Drawing.Size(391, 21)
        self._textBoxELFPath.TabIndex = 19
        # 
        # textBoxRPXPath
        # 
        self._textBoxRPXPath.Location = System.Drawing.Point(24, 31)
        self._textBoxRPXPath.Name = "textBoxRPXPath"
        self._textBoxRPXPath.Size = System.Drawing.Size(391, 21)
        self._textBoxRPXPath.TabIndex = 18
        # 
        # tabPage3
        # 
        self._tabPage3.Controls.Add(self._label8)
        self._tabPage3.Location = System.Drawing.Point(4, 22)
        self._tabPage3.Name = "tabPage3"
        self._tabPage3.Padding = System.Windows.Forms.Padding(3)
        self._tabPage3.Size = System.Drawing.Size(493, 262)
        self._tabPage3.TabIndex = 2
        self._tabPage3.Text = "DS"
        self._tabPage3.UseVisualStyleBackColor = True
        # 
        # tabPage4
        # 
        self._tabPage4.Controls.Add(self._richTextBox1)
        self._tabPage4.Location = System.Drawing.Point(4, 22)
        self._tabPage4.Name = "tabPage4"
        self._tabPage4.Padding = System.Windows.Forms.Padding(3)
        self._tabPage4.Size = System.Drawing.Size(493, 262)
        self._tabPage4.TabIndex = 3
        self._tabPage4.Text = "About"
        self._tabPage4.UseVisualStyleBackColor = True
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(24, 203)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(147, 21)
        self._label7.TabIndex = 33
        self._label7.Text = "Title ID:"
        # 
        # textBoxTitleID
        # 
        self._textBoxTitleID.Location = System.Drawing.Point(186, 203)
        self._textBoxTitleID.Name = "textBoxTitleID"
        self._textBoxTitleID.Size = System.Drawing.Size(121, 21)
        self._textBoxTitleID.TabIndex = 34
        # 
        # richTextBox1
        # 
        self._richTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._richTextBox1.Enabled = False
        self._richTextBox1.Location = System.Drawing.Point(3, 6)
        self._richTextBox1.Name = "richTextBox1"
        self._richTextBox1.ReadOnly = True
        self._richTextBox1.Size = System.Drawing.Size(484, 250)
        self._richTextBox1.TabIndex = 0
        self._richTextBox1.Text = "Nintendo Wiiu VC Injecter.\ngithub:https://github.com/wmltogether"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(6, 12)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 0
        self._label4.Text = "Uncompleted!"
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(6, 12)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 23)
        self._label8.TabIndex = 0
        self._label8.Text = "Uncompleted!"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(525, 454)
        self.Controls.Add(self._tabControl1)
        self.Controls.Add(self._richTextBoxCurrentVC)
        self.Controls.Add(self._label6)
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
        self.Name = "MainForm"
        self.StartPosition = System.Windows.Forms.FormStartPosition.Manual
        self.Text = "VinjeCtiine"
        self.TopMost = True
        self._tabControl1.ResumeLayout(False)
        self._tabPage1.ResumeLayout(False)
        self._tabPage1.PerformLayout()
        self._tabPage2.ResumeLayout(False)
        self._tabPage3.ResumeLayout(False)
        self._tabPage4.ResumeLayout(False)
        self.ResumeLayout(False)


    def ButtonSelectRPXPathClick(self, sender, e):
        dialog = OpenFileDialog()
        dialog.Filter = "WiiU RPX# files (*.rpx)|*.rpx"
        if dialog.ShowDialog(self) == DialogResult.OK and len(dialog.FileName) > 0:
            self._textBoxRPXPath.Text = dialog.FileName
        pass


    def ButtonSelectELFPathClick(self, sender, e):
        dialog = OpenFileDialog()
        dialog.Filter = "WiiU ELF# files (*.elf)|*.elf"
        if dialog.ShowDialog(self) == DialogResult.OK and len(dialog.FileName) > 0:
            self._textBoxELFPath.Text = dialog.FileName
            self.AsyncWrite()
        pass
    
    def ButtonSelectDestRPXPathClick(self, sender, e):
        dialog = SaveFileDialog()
        dialog.Filter = "RPX# files (*.rpx)|*.rpx"
        if dialog.ShowDialog(self) == DialogResult.OK and len(dialog.FileName) > 0:
            self._textBoxDestRPXPath.Text = dialog.FileName
        pass
    
    def AsyncWrite(self):
        dispatcher = Dispatcher.CurrentDispatcher
        DispatcherExtensions.BeginInvoke(dispatcher, Action(self.CheckVCContainer))
        pass
    
    def CheckVCContainer(self):
        import util
        vc = util.VC()
        (WUP_Title,hasNES_ROM ,hasSNES_ROM ,container_size) = vc._checkCurrnetVC(self._textBoxELFPath.Text)
        text = u"[ROM TITLE]:%s;\n"%WUP_Title
        text += u"[ROM TYPE]:NES -> %s ;SNES -> %s\n"%(hasNES_ROM ,hasSNES_ROM)
        text += u"[ROM SIZE]:%d k\n"%(container_size / 1024)
        if hasNES_ROM == False and hasSNES_ROM == False:
            text += u"ERROR:NOT A VALID (S)NES VC!"
            self._buttonStartInject.Enabled = False
        self._textBoxTitleID.Text = WUP_Title
        self._richTextBoxCurrentVC.Text = text
        pass

    def ButtonSelectROMPathClick(self, sender, e):
        dialog = OpenFileDialog()
        dialog.Filter = "ROM files (*.*)|*.*"
        if dialog.ShowDialog(self) == DialogResult.OK and len(dialog.FileName) > 0:
            self._textBoxSelectROMPath.Text = dialog.FileName
        pass

    def ButtonStartInjectClick(self, sender, e):
        import util
        vc = util.VC()
        ROM_NAME = self._textBoxSelectROMPath.Text
        RPX_NAME = self._textBoxRPXPath.Text
        ELF_NAME = self._textBoxELFPath.Text
        DEST_RPX_NAME = self._textBoxDestRPXPath.Text
        try:
            result = vc._NES_Inject(ROM_NAME , RPX_NAME , ELF_NAME , DEST_RPX_NAME)
        except Exception as e:
            print(e)
            result = 4
        if result == 0:
            MessageBox.Show(u"Inject complete!")
        elif result == 1:
            MessageBox.Show(u"Error VC Zlib chunk is tool small!")
        elif result == 2:
            MessageBox.Show(u"Error VC container is tool small!")
        elif result == 3:
            MessageBox.Show(u"Rodata position error!")
        else:
            MessageBox.Show(u"Unknown Error!")
        pass