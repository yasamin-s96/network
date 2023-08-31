import Container from "../components/Container"
import Card from "../components/Card"
const Register = () => {
    return (
        <Container>
            <Card>
                <form className="w-full flex flex-col items-center justify-center space-y-3">
                    <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Firstname" />
                    <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Lastname" />
                    <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Username" />
                    <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="email" placeholder="Email" />
                    <input className="block w-full bg-indigo-300 rounded-lg p-2" type="submit" value={"Sign Up"} />
                </form>
            </Card>
        </Container>
    )
}

export default Register