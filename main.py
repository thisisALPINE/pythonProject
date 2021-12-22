# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
from datetime import date


def validate_field(choices, message):
    while True:
        user_input = input(message)
        if user_input in choices or user_input == 'MENU':
            print(user_input)
            return user_input


def main():
    employees = ['Abigail', 'Emma', 'Lauren', 'Michelangelo']
    priorities = ['1', '2', '3']
    divisions = ['Tech', 'HR', 'Exec']
    statuses = ['Not opened', 'Work in progress', 'Done']
    entities = ['Charity', 'Bank', 'Fund']

    menu_str = "1: Show all records\n" + \
               "2: Add a new record\n" + \
               "3: Amend an existing record\n" + \
               "4: Delete a record\n" + \
               "5: Display full details of a record\n" + \
               "6: Display the menu"

    print(menu_str)
    # Infinite loop
    while True:
        # Step 1: Take the input from the user
        input_str = input("Please select one of the available choices: ")
        input_str = int(input_str)
        print("")
        # Step 2: validate the input
        if input_str < 1 or input_str > 6:
            # Check that the user input is an existing option
            print("Please enter an appropriate option")
        else:
            if input_str == 1:
                # Show all records
                f = open('ds.csv', 'r')
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    print(" ".join(row))
                f.close()

            elif input_str == 2:
                # Add a new record

                # Retrieve last record's number
                f = open('ds.csv', 'r')
                csv_reader = csv.reader(f)
                rows = []
                for row in csv_reader:
                    rows.append(row)
                record_number = int(rows[-1][0]) + 1
                f.close()

                createdBy = validate_field(employees, "Created by: ")
                if createdBy == 'MENU':
                    continue
                dateCreated = date.today().strftime("%d/%m/%Y")
                if dateCreated == 'MENU':
                    continue
                priority = validate_field(priorities, "Priority (1-3): ")
                if priority == 'MENU':
                    continue
                division = validate_field(divisions, "Divisions: ")
                if division == 'MENU':
                    continue
                status = "Not opened"
                assignedTo = validate_field(employees, "Assigned to: ")
                if assignedTo == 'MENU':
                    continue
                entity = validate_field(entities, "Entity: ")
                if entity == 'MENU':
                    continue

                f = open('ds.csv', 'a')
                csv_writer = csv.writer(f)
                csv_writer.writerow(
                    [record_number, createdBy, dateCreated, priority, division, status, assignedTo, entity])
                f.close()

            elif input_str == 3:
                # Amend an existing record
                record_number = input("Record number to be amended: ")
                if record_number == 'MENU':
                    continue
                record_number = int(record_number)

                f = open('ds.csv', 'r')
                csv_reader = csv.reader(f)
                lines = list(csv_reader)
                record_found = False
                for line in lines:
                    if line[0] == record_number:
                        record_found = True
                if not record_found:
                    print("Record not found.")
                    continue

                print("1: Created By\n3: Priority\n4: Division\n5: Status\n6: Assigned To\n7: Entity")
                field_index = input("Field to be changed (index): ")
                if field_index == 'MENU':
                    continue
                field_index = int(field_index)

                # Validate field_index supplied by user
                if field_index == 1 or 3 <= field_index <= 7:
                    if field_index == 1:
                        new_value = validate_field(employees, "Created by: ")
                    elif field_index == 3:
                        new_value = validate_field(priorities, "Priority (1-3): ")
                    elif field_index == 4:
                        new_value = validate_field(divisions, "Divisions: ")
                    elif field_index == 5:
                        new_value = validate_field(statuses, "Status: ")
                    elif field_index == 6:
                        new_value = validate_field(employees, "Assigned to: ")
                    else:
                        new_value = validate_field(entities, "Entity: ")

                    f = open('ds.csv', 'r')
                    csv_reader = csv.reader(f)
                    lines = list(csv_reader)
                    # Change value

                    for line in lines:
                        if line[0] == record_number:
                            line[field_index] = new_value
                    f.close()

                    f = open('ds.csv', 'w')
                    csv_writer = csv.writer(f)
                    csv_writer.writerows(lines)
                    f.close()
                    print("Record successfully changed!")
                else:
                    print("Field index out of range.")

            elif input_str == 4:
                record_number = input("Record number to delete: ")
                if record_number == 'MENU':
                    continue
                # Delete a record
                f = open('ds.csv', 'r')
                csv_reader = csv.reader(f)
                lines = list(csv_reader)
                record_found = False
                for line in lines:
                    if line[0] == record_number:
                        record_found = True
                        lines.remove(line)

                f.close()

                f = open('ds.csv', 'w')
                csv_writer = csv.writer(f)
                csv_writer.writerows(lines)
                f.close()
                if record_found:
                    print("Record successfully deleted!")
                else:
                    print("Record number " + str(record_number) + " doesn't exist.")

            elif input_str == 5:
                # Display full details of a record
                record_number = input("View details of record number: ")
                if record_number == 'MENU':
                    continue
                f = open('ds.csv', 'r')
                csv_reader = csv.reader(f)
                lines = list(csv_reader)
                for line in lines:
                    if line[0] == record_number:
                        print(" ".join(line))
            else:
                print(menu_str)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
