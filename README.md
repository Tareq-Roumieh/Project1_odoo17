Tech Order Exercise

Odoo version: 17

Exercise 1:
    Build Project "training"
    Build Class training.material
        Add Field Name
        Build Views, Action nd Menu
    Build Class training.course
        Add Field Name
        Add Field Number of Student
        Add Field Material
        Build Views, Action nd Menu
---------------------------------------------------
Exercise 2:
    Update Class training.course:
        Add Fields:
            active
            start date
            end date
            duration
            course type (online, onsite)
            responsible
        Build Search View
--------------------------------------------------------
Exercise 3:
    Build Class training.session
        Add field name
        Add field planned_date
        Add field actual_date
        Add Constraint to check planned_date and actual_date
    Update Class training.course
        Add One2many on training.session