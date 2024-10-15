import logging
import time
import requests
from celery import shared_task

from src.apps.order.models import Order

logger = logging.getLogger(__name__)


@shared_task
def process_order_confirmation(order_id):
    try:
        order = Order.objects.get(id=order_id)

        # имитируем подготовку заказа
        time.sleep(5)

        data = {
            "id": str(order.id),
            "amount": float(order.total),
            "date": order.confirmation_time.isoformat(),
        }

        url = "https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4"
        response = requests.post(url, json=data)
        response.raise_for_status()
        logger.info(
            f"Order {order_id} confirmed and webhook sent successfully. Status: {response.status_code}"
        )

    except Order.DoesNotExist:
        logger.error(f"Order {order_id} not found.")
    except requests.RequestException as e:
        logger.error(f"Error sending webhook for order {order_id}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error processing order {order_id}: {e}")
