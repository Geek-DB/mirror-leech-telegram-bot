from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = (f'mirror{CMD_INDEX}', f'm{CMD_INDEX}')
        self.UnzipMirrorCommand = (f'unzipmirror{CMD_INDEX}', f'uzm{CMD_INDEX}')
        self.ZipMirrorCommand = (f'zipmirror{CMD_INDEX}', f'zm{CMD_INDEX}')
        self.QbMirrorCommand = (f'qbmirror{CMD_INDEX}', f'qm{CMD_INDEX}')
        self.QbUnzipMirrorCommand = (f'qbunzipmirror{CMD_INDEX}', f'quzm{CMD_INDEX}')
        self.QbZipMirrorCommand = (f'qbzipmirror{CMD_INDEX}', f'qzm{CMD_INDEX}')
        self.YtdlCommand = (f'ytdl{CMD_INDEX}', f'y{CMD_INDEX}')
        self.YtdlZipCommand = (f'ytdlzip{CMD_INDEX}', f'yz{CMD_INDEX}')
        self.LeechCommand = (f'leech{CMD_INDEX}', f'l{CMD_INDEX}')
        self.UnzipLeechCommand = (f'unzipleech{CMD_INDEX}', f'uzl{CMD_INDEX}')
        self.ZipLeechCommand = (f'zipleech{CMD_INDEX}', f'zl{CMD_INDEX}')
        self.QbLeechCommand = (f'qbleech{CMD_INDEX}', f'ql{CMD_INDEX}')
        self.QbUnzipLeechCommand = (f'qbunzipleech{CMD_INDEX}', f'quzl{CMD_INDEX}')
        self.QbZipLeechCommand = (f'qbzipleech{CMD_INDEX}', f'qzl{CMD_INDEX}')
        self.YtdlLeechCommand = (f'ytdlleech{CMD_INDEX}', f'yl{CMD_INDEX}')
        self.YtdlZipLeechCommand = (f'ytdlzipleech{CMD_INDEX}', f'yzl{CMD_INDEX}')
        self.CloneCommand = f'clone{CMD_INDEX}'
        self.CountCommand = f'count{CMD_INDEX}'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'list{CMD_INDEX}'
        self.SearchCommand = f'search{CMD_INDEX}'
        self.StatusCommand = f'status'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'
        self.LeechSetCommand = f'leechset{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb{CMD_INDEX}'
        self.BtSelectCommand = f'btsel{CMD_INDEX}'
        self.RssListCommand = (f'rsslist{CMD_INDEX}', f'list')
        self.RssGetCommand = (f'rssget{CMD_INDEX}', f'get')
        self.RssSubCommand = (f'rsssub{CMD_INDEX}', f'sub')
        self.RssUnSubCommand = (f'rssunsub{CMD_INDEX}', f'unsub')
        self.RssSettingsCommand = (f'rssset{CMD_INDEX}', f'set')
        self.SleepCommand = f'sleep{CMD_INDEX}'

BotCommands = _BotCommands()
