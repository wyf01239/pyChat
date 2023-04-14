import urwid

text_str = 'Here are a few previous lines.of text that populate.the main terminal window.Press "return" to add the prompt line to the main window.or press escape to exit.'.replace('.', '\n')

def main():
    my_term = MyTerminal()
    urwid.MainLoop(my_term).run()


class MyTerminal(urwid.WidgetWrap):

    def __init__(self):

        self.screen_text = urwid.Text(text_str)
        self.prompt_text = urwid.Edit('prompt: ', '')
        self._w = urwid.Frame(header=urwid.Pile([urwid.Text('header text'),
                             urwid.Divider()]),
                             body=urwid.ListBox([self.screen_text]),
                             footer=self.prompt_text,
                             focus_part='footer')

    def keypress(self, size, key):    
        if key == 'esc':
            raise urwid.ExitMainLoop()
        if key == 'enter':
            self.screen_text.set_text(self.screen_text.text +
                                      '\n' +
                                      self.prompt_text.edit_text)
            self.prompt_text.edit_text = ''
            return
        super(MyTerminal, self).keypress(size, key)

main()