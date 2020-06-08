from django.db import models


# model of form
class MarkyticsForm(models.Model):
    loc = (('corporate_headoffice',"Corporate Headoffice"),('delhi',"Delhi"),('bangalore',"Bangalore"),('kolkata',"Kolkata"))
    location = models.CharField("*Location", max_length=40, choices=loc, default='corporate_headoffice')
    description = models.TextField("*Incident Description")
    date = models.DateField("*Date of Incident")
    time = models.TimeField("*Time of Incident")
    incident_location = models.TextField("Incident Location", blank=True, null=True)
    severity = (('moderate',"Moderate"),('low',"Low"),('high',"High"))
    initial_severity = models.CharField("*Intial severity", max_length=20, choices=severity, default='moderate')
    suspected_cause = models.TextField("Suspected Cause", blank=True, null=True)
    immediate_actions_taken = models.TextField("Immediate Actions Taken", blank=True, null=True)
    is_environmental_incident = models.BooleanField("Environmental Incident", default=False)
    is_injury = models.BooleanField("Injury/Illness", default=False)
    is_property_damage = models.BooleanField("Property Damage", default=False)
    is_vehicle = models.BooleanField("Vehicle", default=False)
    reported_by = models.CharField("*Reported By", max_length=100)

    def __str__(self):
        return self.reported_by
    






