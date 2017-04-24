using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;

namespace SugoiTomodachiQuest {
    class Program {
        public static void Main(String[] argv)
            => new Program().Run().GetAwaiter().GetResult();

        public async Task Run() {
            var discord = new DiscordClient(new DiscordConfig {
                AutoReconnect = true,
                DiscordBranch = Branch.Stable,
                LargeThreshold = 250,
                LogLevel = LogLevel.Unnecessary,
                Token = "",
                TokenType = TokenType.Bot,
                UseInternalLogHandler = false
            });

            await discord.Connect();
            await Task.Delay(-1);
        }
    }
}

