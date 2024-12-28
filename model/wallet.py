from pytoniq import WalletV4R2, Cell
from model.config import AdminWalletConfig


class AdminWallet:

    def __init__(self):

        self.address = AdminWalletConfig.ADDRESS
        self.mnemonic = AdminWalletConfig.MNEMONIC

    
    async def get_wallet_seqno(self): ...


    async def as_wallet_v4r2(self) -> WalletV4R2: 

        return WalletV4R2.from_mnemonic(mnemonics = self.mnemonic)


    async def send_internal_message(self, message: Cell): ...

    async def send_external_message(self, message: Cell): ...

    