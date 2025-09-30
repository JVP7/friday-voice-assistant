from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
)
from livekit.plugins import google
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from tools import get_weather, search_web, send_email
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()


# giving the agent the already pre defined instructions 
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            tools=[search_web, get_weather, send_email],
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=google.LLM(model="gemini-2.0-flash-001", temperature=0.6),
        tts=cartesia.TTS(model="sonic-2", voice="78ab82d5-25be-4f7d-82b3-7ad64e5b85b2"),
        vad=silero.VAD.load(),
        turn_detection= MultilingualModel(),
    )

    # session starts
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` instead for best results
            video_enabled=True,
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))