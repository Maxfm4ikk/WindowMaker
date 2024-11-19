using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Threading;
using System.Windows.Forms;

namespace WindowsMessageApp
{
    public partial class MainForm : Form
    {
        private readonly string[,] translations = new string[2, 15]
        {
            {
                "Создание системных окон", "Количество окон:", "Заголовки окон (через запятую):",
                "Тексты сообщений (через запятую):", "Типы иконок (info, warning, error, через запятую):",
                "Задержка (в секундах, через запятую):", "Тип кнопок (ok, okcancel, yesno):",
                "Введите имя программы (или выберите файл):", "Выбрать программу", "Создать системные окна",
                "Открыть меню сценариев", "Переключиться на английский", "Заголовок:", "Текст:", "Запустить сценарии"
            },
            {
                "Create System Windows", "Number of windows:", "Window titles (comma-separated):",
                "Message texts (comma-separated):", "Icon types (info, warning, error, comma-separated):",
                "Delay (in seconds, comma-separated):", "Button types (ok, okcancel, yesno):",
                "Enter program name (or choose file):", "Choose Program", "Create system windows",
                "Open scenario menu", "Switch to Russian", "Title:", "Text:", "Run scenarios"
            }
        };

        private string currentLanguage = "ru";
        private string selectedProgramPath = "";

        public MainForm()
        {
            InitializeComponent();
            UpdateTexts();
        }

        private void UpdateTexts()
        {
            int langIndex = currentLanguage == "ru" ? 0 : 1;
            this.Text = translations[langIndex, 0];
            lblNumWindows.Text = translations[langIndex, 1];
            lblTitles.Text = translations[langIndex, 2];
            lblMessages.Text = translations[langIndex, 3];
            lblIcons.Text = translations[langIndex, 4];
            lblDelay.Text = translations[langIndex, 5];
            lblButtons.Text = translations[langIndex, 6];
            lblProgramName.Text = translations[langIndex, 7];
            btnChooseProgram.Text = translations[langIndex, 8];
            btnCreateWindows.Text = translations[langIndex, 9];
            btnOpenScenarioMenu.Text = translations[langIndex, 10];
            btnSwitchLanguage.Text = translations[langIndex, 11];
        }

        private void btnSwitchLanguage_Click(object sender, EventArgs e)
        {
            currentLanguage = currentLanguage == "ru" ? "en" : "ru";
            UpdateTexts();
        }

        private void btnChooseProgram_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog
            {
                Filter = "Executable files (*.exe)|*.exe",
                Title = translations[currentLanguage == "ru" ? 0 : 1, 8]
            };

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                selectedProgramPath = ofd.FileName;
                txtProgramName.Text = selectedProgramPath;
            }
        }

        private void RunProgram(string exePath, int delay)
        {
            Thread.Sleep(delay * 1000);
            try
            {
                Process.Start(exePath);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка запуска программы: {ex.Message}");
            }
        }

        private void btnCreateWindows_Click(object sender, EventArgs e)
        {
            string[] titles = txtTitles.Text.Split(',');
            string[] messages = txtMessages.Text.Split(',');
            string[] icons = txtIcons.Text.Split(',');
            string[] delays = txtDelays.Text.Split(',');
            string buttonType = txtButtons.Text;

            int numWindows = int.Parse(txtNumWindows.Text);

            for (int i = 0; i < numWindows; i++)
            {
                string title = titles[i % titles.Length].Trim();
                string message = messages[i % messages.Length].Trim();
                string icon = icons[i % icons.Length].Trim();
                int delay = int.Parse(delays[i % delays.Length]);

                new Thread(() => ShowSystemMessage(title, message, icon, buttonType)).Start();

                if (!string.IsNullOrEmpty(selectedProgramPath))
                {

                    new Thread(() => RunProgram(selectedProgramPath, delay)).Start();
                }
            }
        }

        private void ShowSystemMessage(string title, string text, string iconType, string buttonType)
        {
            uint MB_OK = 0x00000000;
            uint MB_ICONERROR = 0x00000010;
            uint MB_ICONWARNING = 0x00000030;
            uint MB_ICONINFORMATION = 0x00000040;
            uint MB_OKCANCEL = 0x00000001;
            uint MB_YESNO = 0x00000004;

            uint iconFlag = MB_ICONINFORMATION;
            uint buttonFlag = MB_OK;

            if (iconType == "info")
                iconFlag = MB_ICONINFORMATION;
            else if (iconType == "warning")
                iconFlag = MB_ICONWARNING;
            else if (iconType == "error")
                iconFlag = MB_ICONERROR;

            if (buttonType == "okcancel")
                buttonFlag = MB_OKCANCEL;
            else if (buttonType == "yesno")
                buttonFlag = MB_YESNO;

            MessageBox(IntPtr.Zero, text, title, iconFlag | buttonFlag);
        }

        [DllImport("user32.dll", CharSet = CharSet.Unicode)]
        static extern int MessageBox(IntPtr hWnd, string text, string caption, uint type);
    }
}
