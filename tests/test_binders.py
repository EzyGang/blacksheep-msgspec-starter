from typing import Any

import pytest
from pytest_mock import MockerFixture

from app.lib.binders import MsgPackBinder


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'content,expected',
    [
        ('test', 'expected'),
        (None, None),
        ('', None),
    ],
)
async def test_msg_pack_binder(content, expected, mocker: MockerFixture) -> None:
    class Request:
        async def read(self) -> Any:
            return content

    _decode_patch = mocker.patch('app.lib.binders.decode', return_value=expected)

    binder = MsgPackBinder(expected_type=None)

    assert await binder.get_value(request=Request()) == expected

    if expected:
        _decode_patch.assert_called_with(content, type=None)
