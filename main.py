import osmnx.graph

from collectors.era_data_collector import EraDataCollector
from controllers.epoch_controller import EpochController
from services.client_provider_service import ClientProviderService
from services.taxi_provider_service import TaxiProviderService


EraDataCollector.addTaxiList(TaxiProviderService.begin_model_recreate())

era = EpochController(EraDataCollector.taxi_bank, TaxiProviderService, ClientProviderService)

era.begin_new_era(5000, 7200000)
