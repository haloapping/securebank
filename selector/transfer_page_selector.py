TRANSFER_MENU = "//a[@data-testid='sidebar-link-transfer']"

FROM_ACCOUNT_SELECT_OPTION = "//button[@data-testid='transfer-from-select']"
TO_ACCOUNT_SELECT_OPTION = "//button[@data-testid='transfer-to-select']"
AMOUNT_INPUT_TXT = "//input[@data-testid='transfer-amount-input']"
MEMO_INPUT_TXT = "//input[@name='transfer_memo_field']"
TRANSFER_DATE_TODAY_RADIO_BTN = (
    "//input[@type='radio' and @name='dateType' and @value='today']"
)
TRANSFER_DATE_SCHEDULE_RADIO_BTN = (
    "//input[@type='radio' and @name='dateType' and @value='scheduled']"
)
SCHEDULE_DATE_INPUT_TXT = "//input[@data-testid='transfer-scheduled-date-input']"
REVIEW_TRANSFER_BTN = "//button[@data-testid='review-transfer-btn']"
CANCEL_BTN = "//a[@data-testid='cancel-transfer-btn']"

CONFIRM_TRANSFER_BTN = "//button[@data-testid='confirm-transfer-btn']"
CANCEL_TRANSFER_BTN = "//button[@data-testid='cancel-confirm-transfer-btn']"
CLOSE_DIALOG_BTN = "//button[@data-slot='dialog-close']"

BACK_TO_TRANSFER_MENU_BTN = "//a[@data-testid='back-to-dashboard-btn']"
MAKE_ANOTHER_TRANSFER_BTN = "//a[@data-testid='another-transfer-btn']"
