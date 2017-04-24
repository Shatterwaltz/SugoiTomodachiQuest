using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.Logging;

namespace SugoiTomodachiQuest {
    class Program {
        static void Main(string[] args)
            => new Program().MainAsync().GetAwaiter().GetResult();

        public async Task MainAsync() {
        }

        /*private Task Log(LogMessage msg) {
            Console.WriteLine(msg.ToString());
            Task.CompletedTask;
        }*/
   }
}

