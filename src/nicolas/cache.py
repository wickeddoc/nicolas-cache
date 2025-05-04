from typing import Any, Dict, Optional, Iterable

from nicolas.memory import MemoryCache
from nicolas.redis import RedisCache


class Cache:
    """
    A cache implementation with standard cache operations and tag support.
    Supports both in-memory and Redis backends.
    """

    def __init__(self, backend: str = "memory", **kwargs):
        """
        Initialize the cache with the specified backend.

        Args:
            backend: The backend to use ('memory' or 'redis')
            **kwargs: Additional arguments to pass to the backend constructor
        """
        if backend == "memory":
            self._backend = MemoryCache()
        elif backend == "redis":
            self._backend = RedisCache(**kwargs)
        else:
            raise ValueError(f"Unsupported backend: {backend}")

    def get(self, cache_key: str) -> Any:
        """
        Retrieve a value from the cache by key.

        Args:
            cache_key: A unique identifier for the cached item

        Returns:
            The cached value if the key exists, None otherwise
        """
        return self._backend.get(cache_key)

    def get_by_tag(self, tag: str) -> Dict[str, Any]:
        """
        Retrieve all entries in the cache with a specific tag.

        Args:
            tag: The tag to filter cache entries by

        Returns:
            A dictionary containing all matching cache key-value pairs
        """
        return self._backend.get_by_tag(tag)

    def getall(self) -> Dict[str, Any]:
        """
        Retrieve all entries in the cache.

        Returns:
            A dictionary containing all cache key-value pairs
        """
        return self._backend.getall()

    def set(
        self, cache_key: str, value: Any, tags: Optional[Iterable[str]] = None, **kwargs
    ) -> None:
        """
        Store a value in the cache with the given key and optional tags.

        Args:
            cache_key: A unique identifier for the cached item
            value: The value to be stored
            tags: Optional list or set of tags to associate with this cache entry
            **kwargs: Additional backend-specific arguments (e.g., ttl for Redis)
        """
        self._backend.set(cache_key, value, tags=tags, **kwargs)

    def delete(self, cache_key: str) -> bool:
        """
        Remove an entry from the cache by its key.

        Args:
            cache_key: A unique identifier for the cached item

        Returns:
            True if the key was found and deleted, False otherwise
        """
        return self._backend.delete(cache_key)

    def delete_by_tag(self, tag: str) -> int:
        """
        Remove all entries from the cache with a specific tag.

        Args:
            tag: The tag to filter cache entries by

        Returns:
            The number of entries removed
        """
        return self._backend.delete_by_tag(tag)

    def exists(self, cache_key: str) -> bool:
        """
        Check if a key exists in the cache.

        Args:
            cache_key: A unique identifier for the cached item

        Returns:
            True if the key exists in the cache, False otherwise
        """
        return self._backend.exists(cache_key)
