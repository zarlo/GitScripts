using System;
using System.Diagnostics;
using ConsoleDraw;

namespace CosmosUpdaterCSharp
{
    class Program
    {

        
        static void Main(string[] args)
        {

            Process proc = new Process();
            proc.StartInfo.FileName = "cmd.exe";
            proc.StartInfo.Arguments = "dotnet --version";
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.RedirectStandardOutput = true;
            proc.Start();


            if (!proc.StandardOutput.ReadToEnd().StartsWith("2."))
            {



            }

            Console.WriteLine("Hello World!");

            con

        }
    }
}
