def Notes():
    
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnError = True 


    clickButton(waitForObject(":Market-Q (qa)_JButton"))
    activateItem(waitForObjectItem(":Market-Q (qa)_JButton", "Notes"))
    test.compare(waitForObjectExists(":Market-Q (qa).Notes_LCLabel").name, "Notes")
    test.passes("Pass")
    snooze(1)
    
    mouseClick(waitForObject(":Market-Q (qa).Notes_LCLabel"), 11, 0, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Show Window Title"))
    mouseClick(waitForObject(":Market-Q (qa). _LCLabel_2"), 12, 1, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Show Window Title"))
    test.compare(waitForObjectExists(":Market-Q (qa).Notes_LCLabel").text, "Notes")
    
    mouseClick(waitForObject(":Market-Q (qa).Notes_LCLabel"), 16, 2, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "New"))
    activateItem(waitForObjectItem(":Market-Q (qa).New_JMenu_4", "Notes"))
    activateItem(waitForObjectItem(":Notes_JMenu", "To the left"))
    test.compare(waitForObjectExists(":Market-Q (qa).Notes_LCLabel").name, "Notes")
    clickButton(waitForObject(":Market-Q (qa)_JButton_2"))
    
    mouseClick(waitForObject(":Market-Q (qa).Notes_LCLabel"), 17, 2, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Show Titlebar description"))
    test.compare(waitForObjectExists(":Market-Q (qa).Notes_LCLabel_2").text, "Notes")
    snooze(1)
    
    mouseClick(waitForObject(":Market-Q (qa).Notes_LCLabel_2"), 20, 9, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Customize Titlebar Description..."))
    type(waitForObject(":Titlebar Description Settings.Notes_LCTextArea"), "<Right>")
    type(waitForObject(":Titlebar Description Settings.Notes_LCTextArea"), "<Right>")
    type(waitForObject(":Titlebar Description Settings.Notes_LCTextArea"), "<Right>")
    type(waitForObject(":Titlebar Description Settings.Notes_LCTextArea"), "<Right>")
    type(waitForObject(":Titlebar Description Settings.Notes_LCTextArea"), "<Right>")
    type(waitForObject(":Titlebar Description Settings.Notes_LCTextArea"), " test")
    clickButton(waitForObject(":Titlebar Description Settings.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)

    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 25, 7, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Copy Out"))
    mouseClick(waitForObject(":Notes.Notes test_LCLabel"), 19, 6, 4, Button.Button3)
    mouseClick(waitForObject(":Notes.Notes test_LCLabel"), 1273, 12, 0, Button.Button1)
    clickButton(waitForObject(":Notes_JButton"))
    snooze(1)
    
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 26, 14, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Copy Out"))
    test.compare(waitForObjectExists(":Notes.Notes test_LCLabel").text, "Notes test")
    
    mouseClick(waitForObject(":Notes.Notes test_LCLabel"), 1290, 7, 0, Button.Button1)
    clickButton(waitForObject(":Notes_JButton"))
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 24, 6, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Cut Window"))
    mouseClick(waitForObject(":Market-Q (qa).Empty Window_LCLabel"), 31, 0, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Paste Notes"))
    activateItem(waitForObjectItem(":Market-Q (qa).Paste Notes_JMenu", "To the left"))
    clickButton(waitForObject(":Market-Q (qa)_JButton_2"))
    test.compare(waitForObjectExists(":Market-Q (qa).Notes test_LCLabel").text, "Notes test")
    
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 22, 10, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Copy Window"))
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 35, 11, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Paste Notes"))
    activateItem(waitForObjectItem(":Market-Q (qa).Paste Notes_JMenu", "To the left"))
    test.compare(waitForObjectExists(":Market-Q (qa).Notes test_LCLabel").text, "Notes test")
    snooze(1)
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 617, 5, 0, Button.Button1)
    clickButton(waitForObject(":Market-Q (qa)_JButton_2"))
    
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 27, 14, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Copy Window Image"))
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 34, 9, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Paste Notes"))
    activateItem(waitForObjectItem(":Market-Q (qa).Paste Notes_JMenu", "To the left"))
    
    mouseClick(waitForObject(":Market-Q (qa)_JViewport_2"), 404, 371, 0, Button.Button1)
    test.compare(waitForObjectExists(":Market-Q (qa).Notes test_LCLabel").text, "Notes test")
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 567, 13, 0, Button.Button1)
    clickButton(waitForObject(":Market-Q (qa)_JButton_2"))
    
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 29, 5, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Send Image by E-mail..."))
    test.passes("Pass")
    snooze(1)
    
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 19, 8, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Take Custom Screenshot"))
    test.passes("Pass")
    snooze(1)
    
    mouseDrag(waitForObject(":Market-Q (qa).com.futuresource.livecharts.common.LCPanel_LCPanel_3"), 1, 1, 1346, 566, Modifier.None, Button.Button1)
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 17, 10, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Print"))
    clickButton(waitForObject(":Print Notes.OK_FixedSizeButton"))
    clickButton(waitForObject(":Print.Cancel_JButton"))
    test.passes("Pass")
    snooze(1)
    
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 21, 11, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Display Properties"))
    test.compare(waitForObjectExists(":com.futuresource.livecharts.common.LCCardList$1.Text & Colors  _ListItemProxy_4").text, "Text & Colors")
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    snooze(1)
    
    mouseClick(waitForObject(":Market-Q (qa).Notes test_LCLabel"), 18, 14, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Empty"))
    test.passes("Pass")
    snooze(1)
    
    clickButton(waitForObject(":Market-Q (qa)_JButton"))
    activateItem(waitForObjectItem(":Market-Q (qa)_JButton", "Notes"))
    mouseClick(waitForObject(":Market-Q (qa).Notes_LCLabel"), 16, 7, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa)_TitlebarPanel_4", "Close"))
    test.passes("Pass")
    snooze(1)
    
    mouseClick(waitForObject(":Market-Q (qa)_JPanel_8"), 7, 10, 0, Button.Button1)
    clickButton(waitForObject(":Market-Q (qa)_JButton"))
    activateItem(waitForObjectItem(":Market-Q (qa)_JButton", "Notes"))
    clickButton(waitForObject(":Market-Q (qa).Add_FixedSizeButton"))
    type(waitForObject(":Note - _LCTextField"), "IBM")
    mouseClick(waitForObjectItem(":Note - .ComboBox.list_JList", "IBM"), 30, 15, 0, Button.Button1)
    mouseClick(waitForObject(":Note - INTERNATIONAL BUSINESS MACHS_JTextPane"), 47, 19, 0, Button.Button1)
    type(waitForObject(":Note - INTERNATIONAL BUSINESS MACHS_JTextPane"), "IBM Notes")
    clickButton(waitForObject(":Note - INTERNATIONAL BUSINESS MACHS.OK_FixedSizeButton"))
    clickButton(waitForObject(":Market-Q (qa).Add_FixedSizeButton"))
    type(waitForObject(":Note - _LCTextField"), "<#20>")
    type(waitForObject(":Note - _LCTextField"), "MSFT")
    mouseClick(waitForObjectItem(":Note - .ComboBox.list_JList", "MSFT"), 58, 1, 0, Button.Button1)
    mouseClick(waitForObject(":Note - MICROSOFT CORP_LCToggleButton"), 9, 8, 0, Button.Button1)
    mouseClick(waitForObject(":Note - MICROSOFT CORP_LCToggleButton_2"), 8, 14, 0, Button.Button1)
    mouseClick(waitForObject(":Note - MICROSOFT CORP_LCToggleButton_3"), 6, 9, 0, Button.Button1)
    clickButton(waitForObject(":Note - MICROSOFT CORP. _FixedSizeButton"))
    clickButton(waitForObject(":Note - MICROSOFT CORP_FixedSizeButton"))
    type(waitForObject(":Note - MICROSOFT CORP_JTextPane"), "msft NOTES")
    clickButton(waitForObject(":Note - MICROSOFT CORP.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 28, 6, 0, Button.Button1)
    clickButton(waitForObject(":Market-Q (qa).Edit_FixedSizeButton"))
    type(waitForObject(":Note - INTERNATIONAL BUSINESS MACHS_JTextPane"), " TEST")
    clickButton(waitForObject(":Note - INTERNATIONAL BUSINESS MACHS.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    clickButton(waitForObject(":Market-Q (qa).Delete_FixedSizeButton"))
    clickButton(waitForObject(":Question.Yes_FixedSizeButton"))
    test.passes("Pass")
    snooze(1)
    
    clickButton(waitForObject(":Market-Q (qa).Delete All_FixedSizeButton"))
    clickButton(waitForObject(":Question.Yes_FixedSizeButton"))
    test.passes("Pass")
    snooze(1)
    
    clickButton(waitForObject(":Market-Q (qa).Import from CSV_FixedSizeButton"))
    mouseClick(waitForObject(":Open.Look In:_JButton"), 4, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Open.ComboBox.list_JList", "Desktop"), 67, 14, 0, Button.Button1)
    setValue(waitForObject(":Open_JScrollBar"), 181)
    mouseClick(waitForObjectItem(":Open_JList", "symbolnotes.csv"), 63, 6, 0, Button.Button1)
    clickButton(waitForObject(":Open.Open_JButton"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    clickButton(waitForObject(":Market-Q (qa).Add_FixedSizeButton"))
    test.passes("Pass")
    snooze(1)
    
    type(waitForObject(":Note - _LCTextField"), "<#20>")
    type(waitForObject(":Note - _LCTextField"), "IBM")
    mouseClick(waitForObjectItem(":Note - .ComboBox.list_JList", "IBM"), 20, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Note - INTERNATIONAL BUSINESS MACHS_JTextPane"), 42, 25, 0, Button.Button1)
    type(waitForObject(":Note - INTERNATIONAL BUSINESS MACHS_JTextPane"), "TEST")
    clickButton(waitForObject(":Note - INTERNATIONAL BUSINESS MACHS.OK_FixedSizeButton"))
    clickButton(waitForObject(":Market-Q (qa).Add_FixedSizeButton"))
    type(waitForObject(":Note - _LCTextField"), "ORCL")
    mouseClick(waitForObjectItem(":Note - .ComboBox.list_JList", "ORCL"), 29, 12, 0, Button.Button1)
    snooze(1)
    #mouseClick(waitForObject(":_JTextPane"), 69, 24, 0, Button.Button1)
    type(waitForObject(":Note - ORACLE CORP_JTextPane"), "TEST ORCL")
    clickButton(waitForObject(":Note - ORACLE CORP.OK_FixedSizeButton"))
    clickButton(waitForObject(":Market-Q (qa).Export to CSV_FixedSizeButton"))
    type(waitForObject(":Save.File Name:_JTextField"), "NOTES TEST")
    clickButton(waitForObject(":Save.Save_JButton"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 31, 11, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "View"))
    activateItem(waitForObjectItem(":Market-Q (qa).View_JMenu_4", "Chart"))
    test.compare(waitForObjectExists(":Market-Q (qa).Chart_LCLabel").name, "Chart")
    clickButton(waitForObject(":Market-Q (qa)_JButton_3"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 16, 1, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Add To Symbol list"))
    activateItem(waitForObjectItem(":Market-Q (qa).Add To Symbol list_JMenu_5", "Workspace Symbol Lists"))
    activateItem(waitForObjectItem(":Workspace Symbol Lists_JMenu_5", "Global Energy"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 19, 4, 4, Button.Button3)
    clickButton(waitForObject(":Market-Q (qa).Watch List_MonsoonNewPadButton"))
    clickButton(waitForObject(":Market-Q (qa).Symbol List_LCTreeButton"))
    mouseClick(waitForObjectItem(":Market-Q (qa)_LCTree", ".Workspace Symbol Lists.Global Energy"), 70, 7, 0, Button.Button1)
    test.compare(waitForObjectExists(":com.futuresource.livecharts.newquotes.QuotePad$2.17_0_TableItemProxy").text, "IBM")
    clickButton(waitForObject(":Market-Q (qa)_JButton_3"))
    test.passes("Pass")
    snooze(1)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 13, 4, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Add To Symbol list"))
    activateItem(waitForObjectItem(":Market-Q (qa).Add To Symbol list_JMenu_5", "Mobile Home Page (Phone Only)"))
    activateItem(waitForObjectItem(":Mobile Home Page (Phone Only)_JMenu_4", "Futures"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    clickButton(waitForObject(":Market-Q (qa).Watch List_MonsoonNewPadButton"))
    clickButton(waitForObject(":Market-Q (qa).Symbol List_LCTreeButton"))
    mouseClick(waitForObjectItem(":Market-Q (qa)_LCTree", ".Mobile Home Page (Phone Only).Futures"), 55, 7, 0, Button.Button1)
    test.compare(waitForObjectExists(":com.futuresource.livecharts.newquotes.QuotePad$2.13_0_TableItemProxy").text, "IBM")
    clickButton(waitForObject(":Market-Q (qa)_JButton_3"))
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 16, 8, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Add To Symbol list"))
    activateItem(waitForObjectItem(":Market-Q (qa).Add To Symbol list_JMenu_5", "Shared Symbol Lists"))
    activateItem(waitForObjectItem(":Shared Symbol Lists_JMenu_2", "List 1"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    clickButton(waitForObject(":Market-Q (qa).Watch List_MonsoonNewPadButton"))
    clickButton(waitForObject(":Market-Q (qa).Symbol List_LCTreeButton"))
    mouseClick(waitForObjectItem(":Market-Q (qa)_LCTree", ".Shared Symbol Lists.List 1"), 21, 7, 0, Button.Button1)
    test.compare(waitForObjectExists(":com.futuresource.livecharts.newquotes.QuotePad$2.2_0_TableItemProxy").text, "IBM")
    clickButton(waitForObject(":Market-Q (qa)_JButton_3"))
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 20, 3, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Create Expression Shortcut for IBM"))
    type(waitForObject(":Add Expression Shortcut_LCUppercaseTextField"), "Test notes")
    mouseClick(waitForObject(":Add Expression Shortcut_LCTextArea_2"), 92, 41, 0, Button.Button1)
    type(waitForObject(":Add Expression Shortcut_LCTextArea_2"), "test notes")
    clickButton(waitForObject(":Add Expression Shortcut.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 32, 2, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Sort"))
    activateItem(waitForObjectItem(":Market-Q (qa).Sort_JMenu_2", "Sort By Symbol Ascending"))
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 45, 6, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Sort"))
    activateItem(waitForObjectItem(":Market-Q (qa).Sort_JMenu_2", "Sort By Symbol Descending"))
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 22, 5, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Print"))
    clickButton(waitForObject(":Print Notes.OK_FixedSizeButton"))
    clickButton(waitForObject(":Print.Cancel_JButton"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 23, 8, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Defaults"))
    activateItem(waitForObjectItem(":Market-Q (qa).Defaults_JMenu_6", "Save Notes Properties As Default"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 25, 1, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Display Properties..."))
    mouseClick(waitForObject(":Notes Display Properties_CommonButton"), 10, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Notes Display Properties.ComboBox.list_JList", "17"), 20, 13, 0, Button.Button1)
    mouseClick(waitForObject(":Notes Display Properties.Bold_LCCheckBox"), 13, 8, 0, Button.Button1)
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 26, 11, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Defaults"))
    activateItem(waitForObjectItem(":Market-Q (qa).Defaults_JMenu_6", "Save Notes Properties As Default"))
    clickButton(waitForObject(":Question.Yes_FixedSizeButton"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    clickButton(waitForObject(":Market-Q (qa)_JButton_2"))
    clickButton(waitForObject(":Market-Q (qa)_JButton"))
    activateItem(waitForObjectItem(":Market-Q (qa)_JButton", "Notes"))
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 18, 8, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Defaults"))
    activateItem(waitForObjectItem(":Market-Q (qa).Defaults_JMenu_6", "Apply Default Properties to the Notes"))
    test.passes("Pass")
    snooze(1)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 27, 15, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Defaults"))
    activateItem(waitForObjectItem(":Market-Q (qa).Defaults_JMenu_6", "Apply Default Properties to all Notes Windows"))
    clickButton(waitForObject(":Market-Q (qa)_JButton_2"))
    clickButton(waitForObject(":Market-Q (qa)_JButton"))
    activateItem(waitForObjectItem(":Market-Q (qa)_JButton", "Notes"))
    test.passes("Pass")
    snooze(1)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 29, 8, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Defaults"))
    activateItem(waitForObjectItem(":Market-Q (qa).Defaults_JMenu_6", "Remove Default Notes Properties"))
    clickButton(waitForObject(":Question.Yes_FixedSizeButton"))
    clickButton(waitForObject(":Information.OK_FixedSizeButton"))
    clickButton(waitForObject(":Market-Q (qa)_JButton_2"))
    clickButton(waitForObject(":Market-Q (qa)_JButton"))
    activateItem(waitForObjectItem(":Market-Q (qa)_JButton", "Notes"))
    test.passes("Pass")
    snooze(1)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 20, 5, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Display Properties..."))
    test.compare(waitForObjectExists(":com.futuresource.livecharts.common.LCCardList$1.Text & Colors  _ListItemProxy_4").text, "Text & Colors")
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 72, 6, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Display Properties..."))
    mouseClick(waitForObject(":Notes Display Properties_CommonButton_2"), 5, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Notes Display Properties.ComboBox.list_JList", "Times New Roman"), 58, 4, 0, Button.Button1)
    mouseClick(waitForObject(":Notes Display Properties.com.futuresource.livecharts.common.LCComboBox_LCComboBox_2"), 19, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Notes Display Properties.ComboBox.list_JList", "13"), 15, 8, 0, Button.Button1)
    mouseClick(waitForObject(":Notes Display Properties.Bold_LCCheckBox"), 7, 11, 0, Button.Button1)
    mouseClick(waitForObject(":Notes Display Properties.Italic_LCCheckBox"), 10, 6, 0, Button.Button1)
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 19, 5, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Display Properties..."))
    clickButton(waitForObject(":Notes Display Properties. _FixedSizeButton"))
    clickButton(waitForObject(":Notes Display Properties_FixedSizeButton_5"))
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 15, 8, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Display Properties..."))
    clickButton(waitForObject(":Notes Display Properties. _FixedSizeButton_2"))
    clickButton(waitForObject(":Notes Display Properties_FixedSizeButton_6"))
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)

    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 19, 10, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Display Properties..."))
    clickButton(waitForObject(":Notes Display Properties. _FixedSizeButton_3"))
    clickButton(waitForObject(":Notes Display Properties_FixedSizeButton_7"))
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 22, 12, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Display Properties..."))
    mouseClick(waitForObjectItem(":Notes Display Properties.com.futuresource.livecharts.common.LCCardList$1_LCList", "Gridlines  "), 54, 11, 0, Button.Button1)
    mouseClick(waitForObject(":Notes Display Properties.Show Horizontal Gridlines_LCCheckBox"), 8, 14, 0, Button.Button1)
    mouseClick(waitForObject(":Notes Display Properties.Show Vertical Gridlines_LCCheckBox"), 9, 14, 0, Button.Button1)
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)
    
    mouseClick(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "0/0"), 21, 5, 4, Button.Button3)
    activateItem(waitForObjectItem(":Market-Q (qa).com.futuresource.livecharts.notes.NotesTable_NotesTable", "Display Properties..."))
    mouseClick(waitForObject(":Notes Display Properties.Show Horizontal Gridlines_LCCheckBox"), 11, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Notes Display Properties.Show Vertical Gridlines_LCCheckBox"), 8, 7, 0, Button.Button1)
    clickButton(waitForObject(":Notes Display Properties. _FixedSizeButton_4"))
    clickButton(waitForObject(":Notes Display Properties_FixedSizeButton_8"))
    clickButton(waitForObject(":Notes Display Properties.OK_FixedSizeButton"))
    test.passes("Pass")
    snooze(2)

    snooze(40)
    