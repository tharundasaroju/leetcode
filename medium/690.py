class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        total_importance = 0
        employee = self.findEmployeeById(id, employees)
        total_importance = employee.importance
        for subordinate in employee.subordinates:
            total_importance += self.getImportance(employees, subordinate)
        return total_importance
    
    def findEmployeeById(self, id: int, employees: list['Employee']) -> 'Employee':
        for i in range(len(employees)):
            if(employees[i].id == id):
                x = employees.pop(i)
                return x