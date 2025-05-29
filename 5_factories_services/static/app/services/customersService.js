app.service('customersService', function ($http) {
    this.getCustomers = function() {
        return $http.get('/customers');
    };
    this.getCustomer = function(customerId) {
        return $http.get('/customers/' + customerId);
    }
});