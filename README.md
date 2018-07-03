# To-Do
A command-line to-do list manager.

### Prerequisites

Python 3.x

## Usage

* todo : displays to-do list

```bash
$ todo
```

```
                                   TO-DO LIST                                   
================================================================================

	1) Get dry-cleaning
	2) Finish reading to-do/README
```

#### Commands:

* add : adds a new item to the to-do list
    
```bash
$ todo add Buy groceries
```
```
                                   TO-DO LIST                                   
================================================================================

	1) Get dry-cleaning
	2) Finish reading to-do/README
	3) Buy groceries
```
* del : delete an entry

```bash
$ todo del 1
```
```
                                   TO-DO LIST                                   
================================================================================

	1) Finish reading to-do/README
	2) Buy groceries
```
* clear : clear to-do list

```bash
$ todo clear
```
```
                                   TO-DO LIST                                   
================================================================================

	Your todo list is empty!
```

### Notes

The to-do list is stored in a .JSON file in the home folder.

## Authors

* **Naveen Unnikrishnan** - *Initial work* - [naveen-u](https://github.com/naveen-u)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
