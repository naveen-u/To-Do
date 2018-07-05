# To-Do
A command-line to-do list manager.

### Prerequisites

Python 3.x

## Features

- Add and delete one or more items to to-do list.
- Flag to-do list items as URGENT and/or IMPORTANT.
- Tag to-do list items. (Tags are lowercase strings containing no whitespace.) 
- Search for items with specific tags.
- Delete items with specific tags.

## Usage

* todo : displays to-do list

```bash
$ todo
```
![image](https://user-images.githubusercontent.com/29832401/42280282-eeb38fce-7fbd-11e8-8d45-b89992127bb0.png)

Use the option `-v` or `--verbose` to view tags along with the items.

```bash
$ todo -v
```
![image](https://user-images.githubusercontent.com/29832401/42328956-3d9ce5ca-808d-11e8-8585-e946bbfdd790.png)

Use the option `-t` or `--tag` to view items with a particular tag. (NOTE: `-t` assumes everything that follows is a tag, and hence cannot be clubbed with any of the commands below.)

```bash
$ todo -t shopping
```
![image](https://user-images.githubusercontent.com/29832401/42329306-022fc826-808e-11e8-8fbc-ece26b0db884.png)

### Commands:

By default, todo displays the modified to-do list after execution of each of these commands. Use the option `-s` or `--suppress` to suppress this behaviour.

* `add`: Adds new item(s) to the to-do list. Seperate multiple items with `^`. Use the `-u` or `--urgent` option to flag items as URGENT, and `-i` or `--important` to flag items as IMPORTANT. These will be displayed at the top of the to-do list. URGENT entries are denoted by a ❗ and IMPORTANT entries are denoted by a ⭐. To tag items, use `-t` or `--tag` followed by the list of tags (separated by space).
    
```bash
$ todo -s -ui Finish reading this README
$ todo -s add -u Get cake -t shopping
$ todo -v add -i Eat cake ^ Feed the squirrel
```
![image](https://user-images.githubusercontent.com/29832401/42329518-739c05c4-808e-11e8-82e2-2e96c0e4ba6a.png)

* `del`: Deletes entry(ies) from the to-do list. Seperate multiple items with whitespace (although other non-numeric, non-dash characters also work as delimiters, whitespace is preferred for cogency). Give a range of entries to be deleted using a `-`. To delete all items with a particular tag, use the `-t` or `--tag` option. (NOTE: `-t` can be combined with serial numbers of entries to be deleted provided the tags are given at the end. `-t` assumes everything succeeding it is a tag.)

```bash
$ todo del 2-4 -t chores                # deletes entries 2, 3, 4, and all entries with a "chores" tag.
```
![image](https://user-images.githubusercontent.com/29832401/42329937-917fd9ac-808f-11e8-862e-f3d6ed79ce35.png)

* `clear` : Clears to-do list

```bash
$ todo clear
```
![image](https://user-images.githubusercontent.com/29832401/42281475-41f90abc-7fc1-11e8-9222-7600690b86b6.png)

### Notes

- The to-do list is stored in a .JSON file in the home folder.
- Entries are time-stamped and entries with the same flags (URGENT/IMPORTANT/BOTH) are sorted in order of addition.
- All entries added in one go will have the same URGENT/IMPORTANT flags and the same tags.
- The `del` command treats non-numeric, non-dash characters as delimiters. Dashes are treated as delimiters if there aren't                          numbers immediately before and after the dash. For example, `del randomtext1`, `del -1`, `del 1-`, and `del 1` all do the same thing.
- While displaying the to-do list the `-t` option displays entries which have *any* of the tags listed.
- While deleting entries using the `-t` option, all entries with *any* of the given tags are deleted.

## Authors

* **Naveen Unnikrishnan** - [naveen-u](https://github.com/naveen-u)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
