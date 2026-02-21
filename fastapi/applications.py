"""
FastAPI - FastAPI applications.
"""

from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from fastapi.routing import APIRouter


class FastAPI:
    """
    The main FastAPI application class.

    This is the class that you use to create a FastAPI application instance.
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[List[Any]] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
        dependencies: Optional[Sequence[Callable]] = None,
        default_response_class: type = Any,
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = None,
        swagger_ui_init_oauth: Optional[Dict[str, Any]] = None,
        middleware: Optional[Sequence[Any]] = None,
        exception_handlers: Optional[Dict[Union[int, type[Exception]], Callable]] = None,
        on_startup: Optional[Sequence[Callable]] = None,
        on_shutdown: Optional[Sequence[Callable]] = None,
        terms_of_service: Optional[str] = None,
        contact: Optional[Dict[str, Union[str, Any]]] = None,
        license_info: Optional[Dict[str, Union[str, Any]]] = None,
        openapi_prefix: str = "",
        root_path: str = "",
        root_path_in_servers: bool = True,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        callbacks: Optional[List[Dict[str, Any]]] = None,
        webhooks: Optional["FastAPI"] = None,
    ) -> None:
        """
        Initialize a FastAPI application.

        Args:
            debug: Enable debug mode.
            routes: List of routes.
            title: Title of the API.
            description: Description of the API.
            version: Version of the API.
            openapi_url: URL for the OpenAPI schema.
            openapi_tags: Tags for the OpenAPI schema.
            servers: List of servers.
            dependencies: Global dependencies.
            default_response_class: Default response class.
            docs_url: URL for the Swagger UI docs.
            redoc_url: URL for the ReDoc docs.
            swagger_ui_oauth2_redirect_url: OAuth2 redirect URL.
            swagger_ui_init_oauth: OAuth2 configuration.
            middleware: List of middleware.
            exception_handlers: Exception handlers.
            on_startup: Startup event handlers.
            on_shutdown: Shutdown event handlers.
            terms_of_service: Terms of service.
            contact: Contact information.
            license_info: License information.
            openapi_prefix: Prefix for OpenAPI URLs.
            root_path: Root path for the application.
            root_path_in_servers: Include root path in servers.
            responses: Default responses.
            callbacks: Callbacks.
            webhooks: Webhooks application.
        """
        self.debug = debug
        self.routes = routes or []
        self.title = title
        self.description = description
        self.version = version
        self.openapi_url = openapi_url
        self.openapi_tags = openapi_tags
        self.servers = servers
        self.dependencies = dependencies or []
        self.default_response_class = default_response_class
        self.docs_url = docs_url
        self.redoc_url = redoc_url
        self.swagger_ui_oauth2_redirect_url = swagger_ui_oauth2_redirect_url
        self.swagger_ui_init_oauth = swagger_ui_init_oauth
        self.middleware = middleware or []
        self.exception_handlers = exception_handlers or {}
        self.on_startup = on_startup or []
        self.on_shutdown = on_shutdown or []
        self.terms_of_service = terms_of_service
        self.contact = contact
        self.license_info = license_info
        self.openapi_prefix = openapi_prefix
        self.root_path = root_path
        self.root_path_in_servers = root_path_in_servers
        self.responses = responses
        self.callbacks = callbacks
        self.webhooks = webhooks
        self.router = APIRouter()

    def include_router(
        self,
        router: "APIRouter",
        *,
        prefix: str = "",
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[Callable]] = None,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        default_response_class: Optional[type] = None,
        callbacks: Optional[List[Dict[str, Any]]] = None,
        generate_unique_id_function: Callable[..., str] = None,
    ) -> None:
        """
        Include an APIRouter in the application.

        Args:
            router: The APIRouter to include.
            prefix: Path prefix for the router.
            tags: Tags for the router.
            dependencies: Dependencies for the router.
            responses: Default responses.
            deprecated: Whether the router is deprecated.
            include_in_schema: Whether to include in the OpenAPI schema.
            default_response_class: Default response class.
            callbacks: Callbacks.
            generate_unique_id_function: Function to generate unique IDs.
        """
        self.router.include_router(
            router,
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            responses=responses,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            default_response_class=default_response_class,
            callbacks=callbacks,
            generate_unique_id_function=generate_unique_id_function,
        )

    def get(self, path: str, **kwargs: Any) -> Callable:
        """Register a GET route."""
        return self.router.get(path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> Callable:
        """Register a POST route."""
        return self.router.post(path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> Callable:
        """Register a PUT route."""
        return self.router.put(path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Callable:
        """Register a DELETE route."""
        return self.router.delete(path, **kwargs)

    def patch(self, path: str, **kwargs: Any) -> Callable:
        """Register a PATCH route."""
        return self.router.patch(path, **kwargs)
