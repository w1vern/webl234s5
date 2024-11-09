<script setup>
const emit = defineEmits(["increment", "decrement"])

const props = defineProps(
	{
		max_value: Number,
		set_count_func: Function
	}
)
const model_value = defineModel()

function increment() {
	if (model_value.value >= props.max_value) return
	props.set_count_func(model_value.value + 1)
	emit("increment")
}

function decrement() {
	if (model_value.value <= 0) return
	props.set_count_func(model_value.value - 1)
	emit("decrement")
}
</script>

<template>
	<InputGroup>
		<InputGroupAddon>
			<Button class="button" label="-" severity="secondary" @click="decrement" />
		</InputGroupAddon>
		<InputGroupAddon>
			<p class="value">
				{{ model_value }}
			</p>
		</InputGroupAddon>
		<InputGroupAddon>
			<Button class="button" label="+" severity="secondary" @click="increment" />
		</InputGroupAddon>
	</InputGroup>
</template>

<style scoped>
.value {
	font-size: 1.5rem;
	color: var(--p-surface-950);
}

.button {
	color: var(--p-surface-950);
	font-size: 1.2rem;
}


</style>
