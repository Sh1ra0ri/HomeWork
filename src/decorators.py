from typing import Any, Callable, Optional
def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """декоратор, который будет автоматически логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""
    def decorator(func: Callable) -> Callable:

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                result = None

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)

            return result

        return wrapper

    return decorator


@log(filename="log.txt")
def my_function(x: int, y: int) -> int:
    return x + y