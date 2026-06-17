const EmployeeCard = ({employee}) => {
    return (
        <div>
            <div>{employee.fullname}</div>
            <div>{employee.phoneNumber}</div>
            <div>{employee.position}</div>
        </div>
    );
};

export default EmployeeCard;