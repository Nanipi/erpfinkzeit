from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
        {
            "label": _("Sales Dashbaord"),
            "icon": "fa fa-money",
            "items": [
                   {
                       "type": "page",
                       "name": "sales_dashboard",
                       "label": _("Sales Dashboard"),
                       "description": _("Sales Dashboard")
                   },
                   {
                       "type": "report",
                       "doctype": "GL Entry",
                       "name": "Deckungsbeitrag",
                       "label": _("Deckungsbeitrag"),
                       "description": _("Deckungsbeitrag"),
                       "is_query_report": True
                   },
                   {
                       "type": "doctype",
                       "name": "Budget Overhead",
                       "label": _("Budget Overhead"),
                       "description": _("Budget Overhead")
                   }
            ]
        },
        {
            "label": _("Lizenzen"),
            "icon": "fa fa-file-text-o",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Licence",
                       "label": _("Licence"),
                       "description": _("Licence")
                   },
                   {
                       "type": "doctype",
                       "name": "Invoice Cycle Log",
                       "label": _("Invoice Cycle Log"),
                       "description": _("Invoice Cycle Log")
                   },
                   {
                       "type": "doctype",
                       "name": "Retailer",
                       "label": _("Retailer"),
                       "description": _("Retailer")
                   }
            ]
        },
        {
            "label": _("Lists"),
            "icon": "octicon octicon-list-ordered",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Beschriftung",
                       "label": _("Beschriftung"),
                       "description": _("Beschriftung")
                   },
                   {
                       "type": "doctype",
                       "name": "Seriennummer",
                       "label": _("Seriennummer"),
                       "description": _("Seriennummer")
                   },
                   {
                       "type": "doctype",
                       "name": "Wartungsvertrag",
                       "label": _("Wartungsvertrag"),
                       "description": _("Wartungsvertrag")
                   },
                   {
                       "type": "doctype",
                       "name": "Parkordnung",
                       "label": _("Parkordnung"),
                       "description": _("Parkordnung")
                   }
            ]
        },
        {
            "label": _("Finanzbuchhaltung"),
            "icon": "octicon octicon-repo",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Kassa",
                       "label": _("Kassa"),
                       "description": _("Kassa")
                   },
                   {
                       "type": "doctype",
                       "name": "Buchhaltungsperiode",
                       "label": _("Buchhaltungsperiode"),
                       "description": _("Buchhaltungsperiode")
                   },
                   {
                       "type": "doctype",
                       "name": "Payment Reminder",
                       "label": _("Payment Reminder"),
                       "description": _("Payment Reminder")
                   },
                   {
                       "type": "doctype",
                       "name": "Direct Debit Proposal",
                       "label": _("Direct Debit Proposal"),
                       "description": _("Direct Debit Proposal")
                   },
                   {
                       "type": "doctype",
                       "name": "Payment Proposal",
                       "label": _("Payment Proposal"),
                       "description": _("Payment Proposal")
                   },
                   {
                       "type": "page",
                       "name": "bank_wizard",
                       "label": _("Bank Wizard"),
                       "description": _("Bank Wizard")
                   },
                   {
                       "type": "doctype",
                       "name": "Rechtliches Dokument",
                       "label": _("Rechtliches Dokument"),
                       "description": _("Rechtliches Dokument")
                   },
                   {
                       "type": "doctype",
                       "name": "Dokumententyp",
                       "label": _("Dokumententyp"),
                       "description": _("Dokumententyp")
                   }
            ]
        },
        {
            "label": _("Integration"),
            "icon": "octicon octicon-broadcast",
            "items": [
                   {
                       "type": "doctype",
                       "name": "ZSW",
                       "label": _("ZSW"),
                       "description": _("ZSW")
                   },
                   {
                       "type": "doctype",
                       "name": "SoftCard File",
                       "label": _("SoftCard File"),
                       "description": _("SoftCard File")
                   },
                   {
                       "type": "doctype",
                       "name": "Calendar Feed Settings",
                       "label": _("Calendar Feed Settings"),
                       "description": _("Calendar Feed Settings")
                   }
            ]
        },
        {
            "label": _("Reports"),
            "icon": "octicon octicon-repo",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Report",
                       "label": _("Report"),
                       "description": _("Report")
                   }
            ]
        }
    ]
