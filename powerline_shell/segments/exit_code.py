from ..utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        if self.powerline.args.prev_error == 0:
            fg = self.powerline.theme.CMD_PASSED_FG
            bg = self.powerline.theme.CMD_PASSED_BG
            self.powerline.append(' %s ' % str(self.powerline.args.prev_error), fg, bg)
            return
        fg = self.powerline.theme.CMD_FAILED_FG
        bg = self.powerline.theme.CMD_FAILED_BG
        self.powerline.append(' %s ' % str(self.powerline.args.prev_error), fg, bg)
