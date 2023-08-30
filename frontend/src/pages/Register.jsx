import Container from "../components/Container"
import Card from "../components/Card"
const Register = () => {
    return (
        <Container>
            <Card>
                <form className="w-full flex flex-col items-center justify-center space-y-3">
                    <input className="w-full py-2" type="text" placeholder="Firstname" />
                    <input className="w-full py-2" type="text" placeholder="Lastname" />
                    <input className="w-full py-2" type="text" placeholder="Username" />
                    <input className="w-full py-2" type="email" placeholder="Email" />
                </form>
            </Card>
        </Container>
    )
}

export default Register