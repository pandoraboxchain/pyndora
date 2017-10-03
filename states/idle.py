from states.base import State
from states.valodating_data import ValodatingData
from states.events.cognitive_job_created import CognitiveJobCreated
from states.events.validation_started import ValidationStarted

class Idle(State):

    def on_event(self, event):
        if type(event) == CognitiveJobCreated:
            contract = event.contract
            count = contract.call().activeWorkersCount()
            for item in range(count):
                worker = contract.call().activeWorkers(item)
                    if worker == self.config['worker']:
                        self.change_state(ValodatingData())
                        self.worker.state.on_event(ValidationStarted(contract, event.address))
        return self
