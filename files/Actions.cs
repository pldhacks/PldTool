using System.Diagnostics;
using System.Threading;
using System.IO;
using System.Linq;
using System;

namespace Fixer
{
    class Program
    {
        static void run(string command){
            var startInfo = new ProcessStartInfo
            {
                FileName = "cmd.exe",
                Arguments = "/C " + command,
                WindowStyle = ProcessWindowStyle.Hidden,
                CreateNoWindow = true,
                UseShellExecute = false
            };

            Process.Start(startInfo);
        }

        static void admin(){
            var path = "\\Users\\";

            string[] users = Directory.GetDirectories(path).Select(
                dir => dir.Remove(0, 7)
            ).ToArray();
            Console.WriteLine("Users:");

            var toPrint = users
              .Select((value, index) => $"{index}) {value}");

            Console.WriteLine(string.Join(Environment.NewLine, toPrint)+Environment.NewLine);

            Console.WriteLine("Which user do you want to admin?");
            Console.Write("> ");
            int chosen=int.Parse(Console.ReadLine());

            run("net localgroup /add Administrators "+users[chosen]);

            Console.WriteLine("Done!");
        }

        static void Main(string[] args)
        {
            while (true){
                Console.WriteLine("What do you want to do?");
                Console.WriteLine("1) Open minesweeper");
                Console.WriteLine("2) Admin a user (fix broken hacked users)");
                Console.WriteLine("3) *Open command prompt (Only works in admin accounts or login screen)");

                Console.Write("> ");
                int chosen=int.Parse(Console.ReadLine());

                switch (chosen){
                    case 1:
                        run("\\Windows\\System32\\winmineXP.exe");
                        break;
                    case 2:
                        admin();
                        break;
                    case 3:
                        run("conhost");
                        break;
                    default: 
                        Console.WriteLine("Invalid selection!");
                        break;
                };
            }
        }
    }
}