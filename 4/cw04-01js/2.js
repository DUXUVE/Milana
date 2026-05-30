class Employee {
    constructor(name) {
        this.name = name;
    }
}

class Company {
    constructor(companyName) {
        this.companyName = companyName;
        this.staff = [];
    }

    hire(...employees) {
        this.staff.splice(this.staff.length - 1, 0, ...employees);
    }

    dismiss(employee) {
        const index = this.staff.indexOf(employee);
        this.staff.splice(index, 1);
    }

    check(employee) {
        return this.staff.includes(employee);
    }
}

const company = new Company("Comp");
const emp1 = new Employee("Aaa");
const emp2 = new Employee("Bbb");
company.hire(emp1, emp2);
company.dismiss(emp2);
company.check(emp2);
