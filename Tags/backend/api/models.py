from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    house_block_lot_no = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    subdivision_village = models.CharField(max_length=100, blank=True, null=True)
    barangay = models.CharField(max_length=100, blank=True, null=True)
    city_municipality = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    residential_address = models.TextField(blank=True, null=True)
    perm_house_block_lot_no = models.CharField(max_length=100, blank=True, null=True)
    perm_street = models.CharField(max_length=100, blank=True, null=True)
    perm_subdivision_village = models.CharField(max_length=100, blank=True, null=True)
    perm_barangay = models.CharField(max_length=100, blank=True, null=True)
    perm_city_municipality = models.CharField(max_length=100, blank=True, null=True)
    perm_province = models.CharField(max_length=100, blank=True, null=True)
    perm_address = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    bloodtype = models.CharField(max_length=3, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    civil_status = models.CharField(max_length=20, blank=True, null=True)
    gsis_id_no = models.CharField(max_length=50, blank=True, null=True)
    pagibig_id_no = models.CharField(max_length=50, blank=True, null=True)
    philhealth_no = models.CharField(max_length=50, blank=True, null=True)
    sss_no = models.CharField(max_length=50, blank=True, null=True)
    tin_no = models.CharField(max_length=50, blank=True, null=True)
    agency_employee_no = models.CharField(max_length=50, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)
    telephone_no = models.CharField(max_length=20, blank=True, null=True)
    spouse_surname = models.CharField(max_length=100, blank=True, null=True)
    spouse_first_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_middle_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_occupation = models.CharField(max_length=100, blank=True, null=True)
    spouse_employer_business_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_business_address = models.TextField(max_length=255, blank=True, null=True)
    spouse_telephone_no = models.CharField(max_length=20, blank=True, null=True)
    children_names = models.TextField(blank=True, null=True) 
    children_date_of_birth = models.TextField(blank=True, null=True)
    father_surname = models.CharField(max_length=100, blank=True, null=True)
    father_first_name = models.CharField(max_length=100, blank=True, null=True)
    father_middle_name = models.CharField(max_length=100, blank=True, null=True)
    mother_maiden_surname = models.CharField(max_length=100, blank=True, null=True)
    mother_maiden_first_name = models.CharField(max_length=100, blank=True, null=True)
    mother_maiden_middle_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
