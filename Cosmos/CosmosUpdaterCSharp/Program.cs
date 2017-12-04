using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace CosmosUpdaterCSharp
{
    class Program
    {


        static string IL2CPU = "https://github.com/CosmosOS/IL2CPU.git";
        static string XSharp = "https://github.com/CosmosOS/XSharp.git";
        static string Cosmos = "https://github.com/CosmosOS/Cosmos.git";

        static void Main(string[] args)
        {
            update(Cosmos, "Cosmos");
            update(XSharp, "XSharp");
            update(IL2CPU, "IL2CPU");
            while (true)
            {
            }

        }

        static void Git(string GitCommand, string Path)
        {
            ProcessStartInfo gitInfo = new ProcessStartInfo();
            gitInfo.CreateNoWindow = true;
            gitInfo.RedirectStandardError = true;
            gitInfo.RedirectStandardOutput = true;
            gitInfo.UseShellExecute = false;
            gitInfo.FileName = "git";
            Process gitProcess = new Process();
            gitInfo.Arguments = GitCommand;
            gitInfo.WorkingDirectory = Path;

            gitProcess.StartInfo = gitInfo;
            gitProcess.Start();

            gitProcess.WaitForExit();
            gitProcess.Close();
            
        }

        static void update(string git, string Path)
        {

            Path = Environment.CurrentDirectory + "\\" + Path;

            if (!System.IO.Directory.Exists(Path))
            {
                System.IO.Directory.CreateDirectory(Path);
                Console.WriteLine("Cloning " + git);
                Git("Clone " + git, Path);
            }
            else
            {
                Console.WriteLine("Updating " + git);
                Git("Push " + git, Path);
            }



        }

    }
}
