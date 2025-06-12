# 🛠️ Project: Python Website Blocker

# 📌 What It Does

Blocks specified websites during working hours by editing the system's  `hosts` file.

# 📁 Files and Structure

You only need one main Python file:

~~~bash
website_blocker.py
~~~

# 🧰 Requirements

- Python 3.x

- Admin/root privileges (to modify the `hosts` file)

# 🧠 How It Works

- Modifies the hosts file on your system.

- Redirects websites to 127.0.0.1, essentially blocking them.

- Unblocks them after working hours.

# ⚙️ Location of hosts File

- Windows: `C:\Windows\System32\drivers\etc\hosts`

- Linux/Mac: `/etc/hosts`

 # 🧾 Sample Code

 ~~~bash
website_blocker.py
~~~

# ⚠️ Note

- Run as Admin/root: You’ll need to run the script with administrative privileges.

- Schedule It: Use Task Scheduler (Windows) or `cron` (Linux/macOS) to run it in the background.

 # ✅ Possible Upgrades
 
- GUI using `tkinter` or `PyQt`

- Add/Remove websites dynamically

- Block based on categories (social, entertainment)

- Notifications or logging

# 🎨 Python Website Blocker with GUI (tkinter)
  
✅ Fe
 
- GUI to

- S

- View

- Ru

# 📁 File: `website_blocker_gui.py`

# ⚙️ How to Run

- Run with admin/root permissions.

- Run the script:

~~~bash
python website_blocker_gui.py
~~~
- Add websites, and click Start Blocking.

# 🧠 Optional Enhancements

- Save/load blocked websites list to file

- Customize working hours in GUI

- Tray icon or minimize-to-tray

Auto-start on system boot

# 🛠️ Steps to Convert to a macOS App

**Step 1: Install PyInstaller**

First, you'll need to install PyInstaller to
~~~bash
pip install pyinstaller
~~~
**Step 2: Create**

- Navigate to the directory where y

- Run the following command to create a standalone app (this will generate a `.app` fi)

  ~~~bash
  pyinstaller --onefile --windowed website_blocker_gui.py
  ~~~
- `--onefile`: Pa

- `--windowed`: Preve

This will generate a `dist` folder cwebsite_blocker_.

 ***Ste***
 
Once PyInstaller finishes, you should see a .app file in the `dist directoryWebsite GUI jus

***Step 4:***

- If yo

- Creat (if you

- Open Keychain A andDevelo certi

- Use t
  ~~~bash
  codesign --sign "Developer ID Application: Your Name (Team ID)" path/to/website_blocker_gui.app
  ~~~

  ***Step 5:***
  
If you want to create a downloadable disk image for distribution, you can package the `.app` file `.dmg` file for

- Install `create-dmg`:
~~~bash
npm install -g create-dmg
~~~
- Run th
~~~bash
create-dmg "dist/website_blocker_gui.app" "dist/website_blocker_gui.dmg"
~~~

This will generate a `.dmg` file, w

# 🎉 Y

Now you have a standalone macO that runs yo

 






Unblocks them after working hours.
