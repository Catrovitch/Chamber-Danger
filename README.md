# Chamber Danger

This is a project where I will create a dungeon generator. The idea is to create a very well functioning and semi-simple program which can easily be expanded on in the future or if time allows it. The project is part of the Tiralabra course at University of Helsinki.

## Documentation

### Weekly reports

 - [Week 1](./documentation/week_1_report.md)
 - [Week 2](./documentation/week_2_report.md)
 - [Week 3](./documentation/week_3_report.md)
 - [Week 4](./documentation/week_4_report.md)
 - [week 5](./documentation/week_5_report.md)
 - [week 6](./documentation/week_6_report.md)

### Other

 - [Project Specifications](./documentation/project_specifications.md)
 - [Implementation document](./documentation/implementation_document.md)
 - [Testing document](./documentation/testing_document.md)
 - [User guide](./documentation/user_guide.md)

## Installing

See [User guide](./documentation/user_guide.md) for more in-depth instructions.

 1. Clone or download the project.
 2. Make sure you have the correct version of python installed.
 3. Make sure you have Poetry installed.
 4. Install dependencies with command:
```
Poetry install
```

 5. Start the program with command:

```
Poetry run invoke start
```

 6. Enjoy!
 
## Testing

A coverage-report can be produced with the command:

```bash
poetry run invoke coverage-report
```

