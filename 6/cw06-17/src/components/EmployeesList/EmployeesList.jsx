import { useEffect } from "react";
import EmployeeCard from "../EmployeeCard/EmloyeeCard";
import useDataLoading from "../../hooks/useDataLoading";

const EmployeesList = () => {
    const {data: employees} = useDataLoading("http://http://192.168.110.58/employees");
    
    return (
        <div>
            <h1>Сотрудники</h1>
            <ul>
                {employees.map((employee) => (
                    <li>
                        <EmployeeCard employee={employee} />
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default EmployeesList;