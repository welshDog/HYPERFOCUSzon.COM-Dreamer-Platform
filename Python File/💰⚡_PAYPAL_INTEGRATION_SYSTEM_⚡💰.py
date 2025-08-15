#!/usr/bin/env python3
"""
💰⚡ PAYPAL INTEGRATION SYSTEM ⚡💰

**Mission:** Integrate PayPal payments with your existing empire systems
**Features:** Payment processing, invoice generation, webhook handling
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, Any, Optional

class PayPalPaymentProcessor:
    """💰 PayPal payment processing and integration"""
    
    def __init__(self):
        # Load configuration from empire.env
        self.client_id = os.getenv("PAYPAL_CLIENT_ID", "YOUR_LIVE_CLIENT_ID_HERE")
        self.client_secret = os.getenv("PAYPAL_CLIENT_SECRET", "YOUR_LIVE_CLIENT_SECRET_HERE")
        self.api_url = os.getenv("PAYPAL_API_URL", "https://api-m.paypal.com")
        self.environment = os.getenv("PAYPAL_ENVIRONMENT", "live")
        self.business_email = os.getenv("PAYPAL_BUSINESS_EMAIL", "lyndzwills@gmail.com")
        
        self.access_token = None
        self.token_expires_at = None
        
        # Service pricing from your empire
        self.service_prices = {
            "discord_bot_basic": {"price": 25.00, "description": "Discord Bot - Basic Package"},
            "discord_bot_standard": {"price": 50.00, "description": "Discord Bot - Standard Package"},
            "discord_bot_premium": {"price": 75.00, "description": "Discord Bot - Premium Package"},
            "adhd_consultation": {"price": 150.00, "description": "ADHD Productivity Consultation"},
            "system_setup": {"price": 250.00, "description": "Complete Productivity System Setup"},
            "python_simple": {"price": 75.00, "description": "Python Automation Script - Simple"},
            "python_complex": {"price": 150.00, "description": "Python Automation - Complex"},
            "ai_video_single": {"price": 40.00, "description": "AI Video Creation - Single"},
            "ai_video_package": {"price": 120.00, "description": "AI Video Package - 3 Videos"}
        }
        
        print(f"""
💰⚡ PAYPAL INTEGRATION SYSTEM INITIALIZED ⚡💰
=============================================

Environment: {self.environment.upper()}
API URL: {self.api_url}
Business Email: {self.business_email}

🎯 Available Services: {len(self.service_prices)}
💎 Ready for payment processing!
        """)

    def get_access_token(self) -> Optional[str]:
        """🔑 Get PayPal access token for API calls"""
        
        if self.access_token and self.token_expires_at:
            if datetime.now().timestamp() < self.token_expires_at:
                return self.access_token
        
        # Request new access token
        url = f"{self.api_url}/v1/oauth2/token"
        
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en_US"
        }
        
        data = "grant_type=client_credentials"
        
        try:
            response = requests.post(
                url,
                headers=headers,
                data=data,
                auth=(self.client_id, self.client_secret)
            )
            
            if response.status_code == 200:
                token_data = response.json()
                self.access_token = token_data["access_token"]
                # Set expiration (subtract 60 seconds for safety)
                expires_in = token_data.get("expires_in", 3600) - 60
                self.token_expires_at = datetime.now().timestamp() + expires_in
                
                print("✅ PayPal access token obtained successfully!")
                return self.access_token
            else:
                print(f"❌ Failed to get access token: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error getting access token: {e}")
            return None

    def create_payment_link(self, service_key: str, custom_amount: Optional[float] = None) -> str:
        """💳 Create PayPal.me payment link for service"""
        
        if service_key in self.service_prices:
            amount = custom_amount or self.service_prices[service_key]["price"]
            description = self.service_prices[service_key]["description"]
        else:
            amount = custom_amount or 50.00
            description = f"Custom Service - {service_key}"
        
        # PayPal.me link format
        paypal_me_link = f"https://paypal.me/WelshDog/{amount:.0f}"
        
        print(f"""
💰 PAYMENT LINK CREATED:
Service: {description}
Amount: ${amount}
Link: {paypal_me_link}
        """)
        
        return paypal_me_link

    def create_invoice(self, service_key: str, client_email: str, 
                      client_name: str, custom_amount: Optional[float] = None) -> Dict[str, Any]:
        """📧 Create PayPal invoice for service"""
        
        token = self.get_access_token()
        if not token:
            return {"error": "Could not get access token"}
        
        if service_key in self.service_prices:
            amount = custom_amount or self.service_prices[service_key]["price"]
            description = self.service_prices[service_key]["description"]
        else:
            amount = custom_amount or 50.00
            description = f"Custom Service - {service_key}"
        
        # Invoice creation payload
        invoice_data = {
            "detail": {
                "invoice_number": f"HFZ-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "reference": f"Service: {service_key}",
                "invoice_date": datetime.now().strftime("%Y-%m-%d"),
                "currency_code": "USD",
                "note": f"Thank you for choosing HyperFocus Zone services! Service: {description}",
                "term": "Due on receipt",
                "memo": "ADHD-optimized productivity solutions"
            },
            "invoicer": {
                "name": {"given_name": "Chief", "surname": "Lyndz"},
                "address": {
                    "address_line_1": "39 First Rd, Pen y Fan",
                    "admin_area_2": "Llanelli",
                    "postal_code": "SA15 1PN",
                    "country_code": "GB"
                },
                "email_address": self.business_email,
                "phones": [{"country_code": "44", "national_number": "7123456789"}],
                "website": "https://hyperfocuszone.com",
                "tax_id": "Hyperfocus Zone Ltd",
                "additional_notes": "Professional ADHD productivity services"
            },
            "primary_recipients": [{
                "billing_info": {
                    "name": {"given_name": client_name.split()[0], "surname": " ".join(client_name.split()[1:])},
                    "email_address": client_email
                }
            }],
            "items": [{
                "name": description,
                "description": f"Professional {description.lower()} service with ADHD optimization",
                "quantity": "1",
                "unit_amount": {"currency_code": "USD", "value": str(amount)},
                "tax": {"name": "Service Tax", "percent": "0"}
            }],
            "configuration": {
                "partial_payment": {"allow_partial_payment": False},
                "allow_tip": True,
                "tax_calculated_after_discount": True,
                "tax_inclusive": False
            },
            "amount": {
                "breakdown": {
                    "item_total": {"currency_code": "USD", "value": str(amount)}
                }
            }
        }
        
        url = f"{self.api_url}/v2/invoicing/invoices"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "PayPal-Request-Id": f"HFZ-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        }
        
        try:
            response = requests.post(url, headers=headers, json=invoice_data)
            
            if response.status_code == 201:
                invoice = response.json()
                invoice_id = invoice["id"]
                
                # Send the invoice
                send_url = f"{self.api_url}/v2/invoicing/invoices/{invoice_id}/send"
                send_response = requests.post(send_url, headers=headers, json={
                    "send_to_recipient": True,
                    "send_to_invoicer": True
                })
                
                if send_response.status_code == 202:
                    print(f"✅ Invoice created and sent successfully!")
                    print(f"Invoice ID: {invoice_id}")
                    print(f"Sent to: {client_email}")
                    
                    return {
                        "success": True,
                        "invoice_id": invoice_id,
                        "invoice_url": invoice.get("href"),
                        "amount": amount,
                        "client_email": client_email
                    }
                else:
                    print(f"⚠️ Invoice created but failed to send: {send_response.status_code}")
                    return {
                        "success": True,
                        "invoice_id": invoice_id,
                        "invoice_url": invoice.get("href"),
                        "amount": amount,
                        "send_error": send_response.text
                    }
            else:
                print(f"❌ Failed to create invoice: {response.status_code}")
                print(f"Response: {response.text}")
                return {"error": f"Invoice creation failed: {response.status_code}"}
                
        except Exception as e:
            print(f"❌ Error creating invoice: {e}")
            return {"error": str(e)}

    def generate_payment_buttons_html(self) -> str:
        """🎨 Generate HTML payment buttons for all services"""
        
        html_buttons = []
        
        for service_key, service_data in self.service_prices.items():
            price = service_data["price"]
            description = service_data["description"]
            
            button_html = f"""
<div class="paypal-service-button">
    <h3>{description}</h3>
    <p class="price">${price}</p>
    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
        <input type="hidden" name="cmd" value="_s-xclick">
        <input type="hidden" name="item_name" value="{description}">
        <input type="hidden" name="amount" value="{price}">
        <input type="hidden" name="currency_code" value="USD">
        <input type="hidden" name="business" value="{self.business_email}">
        <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynow_LG.gif" 
               border="0" name="submit" alt="PayPal - Pay Now">
    </form>
    <p><a href="https://paypal.me/WelshDog/{price:.0f}" target="_blank">Quick Pay: paypal.me/WelshDog/{price:.0f}</a></p>
</div>
            """
            html_buttons.append(button_html)
        
        return "\n".join(html_buttons)

    def track_payment(self, payment_id: str) -> Dict[str, Any]:
        """📊 Track payment status"""
        
        token = self.get_access_token()
        if not token:
            return {"error": "Could not get access token"}
        
        url = f"{self.api_url}/v2/payments/payment/{payment_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        
        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                payment_data = response.json()
                return {
                    "success": True,
                    "payment_id": payment_id,
                    "status": payment_data.get("state"),
                    "amount": payment_data.get("transactions", [{}])[0].get("amount", {}),
                    "payer": payment_data.get("payer", {}),
                    "create_time": payment_data.get("create_time")
                }
            else:
                return {"error": f"Failed to track payment: {response.status_code}"}
                
        except Exception as e:
            return {"error": str(e)}

def demonstrate_payment_system():
    """🚀 Demonstrate the PayPal payment system"""
    
    print("🚀 DEMONSTRATING PAYPAL PAYMENT SYSTEM...")
    
    processor = PayPalPaymentProcessor()
    
    # Test 1: Create payment links
    print("\n💰 CREATING PAYMENT LINKS:")
    links = []
    for service in ["discord_bot_basic", "adhd_consultation", "python_simple"]:
        link = processor.create_payment_link(service)
        links.append(link)
    
    # Test 2: Generate HTML buttons
    print("\n🎨 GENERATING HTML PAYMENT BUTTONS:")
    html_buttons = processor.generate_payment_buttons_html()
    
    # Save to file
    with open("generated_payment_buttons.html", "w") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>HyperFocus Zone - Payment Options</title>
    <style>
        .paypal-service-button {{
            border: 1px solid #ddd;
            margin: 15px;
            padding: 20px;
            border-radius: 10px;
            background: #f9f9f9;
        }}
        .price {{
            font-size: 1.5em;
            color: #00aa00;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>💰 HyperFocus Zone - Secure Payments</h1>
    {html_buttons}
</body>
</html>
        """)
    
    print("✅ Payment buttons saved to 'generated_payment_buttons.html'")
    
    # Test 3: Show configuration status
    print(f"""
📊 PAYPAL INTEGRATION STATUS:
=============================

✅ Access Token: {'Available' if processor.get_access_token() else 'Not configured'}
✅ API Environment: {processor.environment}
✅ Business Email: {processor.business_email}
✅ Service Count: {len(processor.service_prices)}

🎯 READY FOR LIVE PAYMENTS!

📋 NEXT STEPS:
1. Update empire.env with your live PayPal credentials
2. Test with small payment ($1-5)
3. Share payment links on all platforms
4. Start accepting payments immediately!

💰 YOUR BILLS SOLUTION IS READY TO ACTIVATE!
    """)

if __name__ == "__main__":
    demonstrate_payment_system()
