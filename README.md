# To-Do
A command-line to-do list manager.

### Prerequisites

Python 3.x

## Usage

* todo : displays to-do list

```bash
$ todo
```
![image](https://user-images.githubusercontent.com/29832401/42280282-eeb38fce-7fbd-11e8-8d45-b89992127bb0.png)

### Commands:

By default, todo displays the modified to-do list after execution of these commands. Use the option `-s` or `--suppress` to suppress this behaviour.

* `add`: Adds new item(s) to the to-do list. Seperate multiple items with `^`. Use the `-u` option to flag items as URGENT, and `-i` to flag items as IMPORTANT. These will be displayed at the top of the to-do list. URGENT entries are denoted by a ❗ and IMPORTANT entries are denoted by a ⭐.
    
```bash
$ todo -s -ui Finish reading this README
$ todo -s add -u Get cake
$ todo add -i Eat cake ^ Feed the squirrel
```
![image](https://user-images.githubusercontent.com/29832401/42280572-bf63080c-7fbe-11e8-9ab5-2bc5a47daacd.png)

* `del`: Deletes entry(ies) from the to-do list. Seperate multiple items with whitespace (although other non-numeric, non-dash characters also work as delimiters, whitespace is preferred for cogency). Give a range of entries to be deleted using a `-`.

```bash
$ todo del 1 3-5
```
![image](https://user-images.githubusercontent.com/29832401/42281376-face54d0-7fc0-11e8-8e18-ce6101f3e8c0.png)

* `clear` : Clears to-do list

```bash
$ todo clear
```
![image](https://user-images.githubusercontent.com/29832401/42281475-41f90abc-7fc1-11e8-9222-7600690b86b6.png)

### Notes

- The to-do list is stored in a .JSON file in the home folder.
- Entries are time-stamped and entries with the same flags (URGENT/IMPORTANT/BOTH) are sorted in order of addition.
- All entries added in one go will have the same URGENT/IMPORTANT flags.
- The `del` command treats non-numeric, non-dash characters as delimiters. Dashes are treated as delimiters if there aren't numbers immediately before and after the dash. For example, `del randomtext1`, `del -1`, `del 1-`, and `del 1` all do the same thing.

## Authors

* **Naveen Unnikrishnan** - [naveen-u](https://github.com/naveen-u)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
