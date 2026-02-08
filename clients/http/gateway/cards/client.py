from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response

class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для создания новой виртуальной карты
    """
    userId: str
    accountId: str

class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для создания новой физической карты
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cars сервиса http-gateway
    """

    def issue_virtual_card(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Cоздание новой виртуальной карты
        :param request: Cловарь с данными новой виртуальной карты
        :return: Ответ от сервера (объект httpx.Response)
        """

        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Cоздание новой физической карты
        :param request: Cловарь с данными новой физической карты
        :return: Ответ от сервера (объект httpx.Response)
        """

        return self.post(f"/api/v1/cards/issue-physical-card", json=request)