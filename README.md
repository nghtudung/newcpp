# ⚡ newcpp – Quick C++ File Generator

`newcpp` is a minimalist command-line tool for quickly generating `.cpp` files based on a predefined template. Perfect for competitive programmers, students, and anyone who wants to save time creating C++ source files.

---

## 🚀 Features

- 📝 Create new `.cpp` file from a template (e.g. `SAMPLE.cpp`)
- 🔁 Automatically replaces template placeholders (like filenames inside comments or compile commands)
- 🪄 Instantly opens the file in VS Code
- 🧃 Lightweight, terminal-friendly, and fast

---

## 📦 Installation

1. **Clone this repo:**

````bash
git clone https://github.com/nghtudung/newcpp.git
````

2. **Make the script executable:**

````bash
chmod +x /path/to/newcpp/newcpp
````

3. **Add an alias to your shell config:**

```bash
# If you're using zsh:
echo 'alias newcpp="/path/to/newcpp/newcpp"' >> ~/.zshrc

# Or for bash:
echo 'alias newcpp="/path/to/newcpp/newcpp"' >> ~/.bash_profile
```

4. **Reload your shell:**

```bash
source ~/.zshrc
# or
source ~/.bash_profile
```

---

## 🧪 Usage

```bash
newcpp hello.cpp
```

➡ This will:

* Copy everything from `SAMPLE.cpp`
* Replace all internal occurrences of `"SAMPLE.cpp"` with `"hello.cpp"`
* Open `hello.cpp` in VS Code

---

## 📁 Structure

```
📁 ~/.../newcpp/
  ├── newcpp.py      # <- The Python script
  └── SAMPLE.cpp     # <- Your template file
```

---

## 🧙 Tips

* Put your own favourite template inside `SAMPLE.cpp`
* Works on macOS (I haven't test on Linux or Windows)

---

## 💌 Example `SAMPLE.cpp`

```cpp
// g++ SAMPLE.cpp -o SAMPLE && ./SAMPLE

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    // Your code here
    return 0;
}
```

---

## 🙇‍♂️ Credits

From [GieJack™](https://www.youtube.com/watch?v=dQw4w9WgXcQ) with love ❤️
Why don't you star this repo?

---