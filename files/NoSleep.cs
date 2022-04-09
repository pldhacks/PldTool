using System.Diagnostics;
using System.Threading;
using System;

namespace NoShut
{
	class Program
	{
		static void Main(string[] args)
		{
			string command = "shutdown /a";

			var startInfo = new ProcessStartInfo
			{
				FileName = "cmd.exe",
				Arguments = "/C " + command,
				WindowStyle = ProcessWindowStyle.Hidden,
				CreateNoWindow = true,
				UseShellExecute = false
			};

			Console.WriteLine("Keep this console open! It stops the pld from shutting down at 11pm :)");

			for (;;){
				Process.Start(startInfo);
				Thread.Sleep(750);
			}
		}
	}
}